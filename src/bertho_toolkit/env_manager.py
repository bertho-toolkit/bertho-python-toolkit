"""
Módulo env_manager
------------------

Fornece a classe EnvManager para gerenciar variáveis de ambiente
armazenadas em um arquivo '.env'. Suporta:

  - Carregar as variáveis do arquivo.
  - Obter, definir e remover variáveis em memória.
  - Buscar variáveis com prefixo.
  - Construir caminhos de pasta a partir de DEFAULT_PROJECT_PATH.
"""

import os
from typing import Dict, Optional
from .terminal_logger import TerminalLogger


class EnvManager:
    """
    Classe para gerenciar variáveis de ambiente em um arquivo '.env'.

    Parâmetros:
      enable_log (bool): se True, ativa logs internos de carregamento.

    Atributos:
      file_path (str): caminho para o arquivo de variáveis (por padrão '../.env').
      env_vars (Dict[str, str]): cache em memória das variáveis carregadas.
      logger (TerminalLogger): logger de terminal para mensagens internas.
    """
    def __init__(self, enable_log: bool = False) -> None:
        self.enable_log = enable_log
        self.file_path: str = '../.env'
        self.env_vars: Dict[str, str] = {}
        self.logger = TerminalLogger(self.enable_log)
        self.load()

    def load(self) -> None:
        """
        Lê o arquivo '.env' e popula self.env_vars.

        - Ignora linhas vazias ou que comecem com '#'.
        - Para cada linha 'CHAVE=VALOR', armazena em env_vars.
        - Se o arquivo não existir, mantém env_vars vazio.
        """
        if not os.path.exists(self.file_path):
            self.env_vars = {}
            return

        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    key, value = key.strip(), value.strip()
                    self.env_vars[key] = value
                    self.logger.LogInternal(f"load.. {key} = {value}")

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Retorna o valor de 'key', ou default se não existir.

        Exemplo:
          get('API_KEY') → 'abcdef' ou None
        """
        return self.env_vars.get(key.replace("'", ""), default)

    def set(self, key: str, value: str) -> None:
        """
        Define ou atualiza 'key' em memória e salva no arquivo.
        """
        self.env_vars[key] = value
        self.save()

    def remove(self, key: str) -> bool:
        """
        Remove 'key' se existir. Retorna True se removida, False caso contrário.
        """
        if key in self.env_vars:
            del self.env_vars[key]
            self.save()
            return True
        return False

    def save(self) -> None:
        """
        Persiste todas as variáveis de env_vars de volta no arquivo '.env'.
        """
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for key, value in self.env_vars.items():
                f.write(f"{key}={value}\n")

    def get_with_prefix(self, prefix: str, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Busca variável combinando prefixo:
          ex: get_with_prefix('CLASS', 'PROJECT_PATH') → valor de 'CLASS_PROJECT_PATH'
        """
        full_key = f"{prefix}_{key}"
        return self.get(full_key, default)

    def get_folder(self, folder_name: str) -> Optional[str]:
        """
        Se existir DEFAULT_PROJECT_PATH, retorna o caminho para uma subpasta:
          ex: DEFAULT_PROJECT_PATH='/home/user/proj'
              get_folder('data') → '/home/user/proj/data'
        """
        default_project = self.get("DEFAULT_PROJECT_PATH")
        if default_project:
            return os.path.join(default_project, folder_name)
        return None
