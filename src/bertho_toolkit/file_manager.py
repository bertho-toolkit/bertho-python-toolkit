"""
Módulo file_manager
-------------------

Fornece a classe FileManager para:

  - Carregar caminhos de projeto, saída e busca a partir de variáveis de ambiente.
  - Listar recursivamente arquivos em um diretório, ignorando arquivos temporários.
  - Ler e escrever arquivos em disco.

Uso típico:

    from bertho_toolkit import FileManager

    fm = FileManager(env_key="CLASS", enable_log=True)
    paths = fm.get_files_in_search_path("subpasta")
    content = FileManager.read_file_content(paths[0])
    FileManager.write_file_content("saida.txt", "conteúdo")
"""
import os
from typing import List
from .env_manager import EnvManager
from .terminal_logger import TerminalLogger

# Arquivos/pastas que não devem ser listados
IGNORED_FILES = {
    '.env', 'local.env', 'env.example',
    '.DS_Store', 'Thumbs.db', '.gitkeep'
}


class FileManager:
    """
    Gerencia operações de arquivo com base em variáveis de ambiente.

    Parâmetros:
      env_key (str): prefixo das variáveis de ambiente (ex.: 'CLASS').
      enable_log (bool): se True, ativa logs de aviso via TerminalLogger.

    Atributos públicos:
      PROJECT_PATH (Optional[str]): caminho base do projeto.
      OUTPUT_PATH  (Optional[str]): caminho de saída de arquivos.
      SEARCH_PATH  (Optional[str]): caminho onde buscar arquivos.
    """

    def __init__(self, env_key: str, enable_log: bool = True) -> None:
        self.env_key = env_key.upper()
        self.logger = TerminalLogger(enable_log)

        # Usa EnvVarManager para carregar .env
        env = EnvManager(enable_log)

        # Busca VARS específicas ou as padrão
        self.PROJECT_PATH = env.get_with_prefix(
            self.env_key, 'PROJECT_PATH', env.get('DEFAULT_PROJECT_PATH')
        )
        self.OUTPUT_PATH = env.get_with_prefix(
            self.env_key, 'OUTPUT_PATH', env.get('DEFAULT_OUTPUT_PATH')
        )
        self.SEARCH_PATH = env.get_with_prefix(
            self.env_key, 'SEARCH_PATH', env.get('DEFAULT_EXTRACTOR_SEARCH_PATH')
        )

    def get_files_in_search_path(self, append_path: str = "") -> List[str]:
        """
        Retorna todos os arquivos sob SEARCH_PATH/append_path, exceto os IGNOREDS.

        Exemplo:
          fm.get_files_in_search_path("data")
        """
        if not self.SEARCH_PATH:
            self.logger.LogError("SEARCH_PATH não configurado.")
            return []

        target = os.path.join(self.SEARCH_PATH, append_path)
        if not os.path.exists(target):
            self.logger.LogWarning(f"Caminho não encontrado: {target}")
            return []

        files_list: List[str] = []
        for root, _, files in os.walk(target):
            for name in files:
                if name in IGNORED_FILES:
                    continue
                files_list.append(os.path.join(root, name))
        return files_list

    @staticmethod
    def read_file_content(file_path: str) -> str:
        """
        Lê todo o conteúdo de um arquivo e retorna como string.

        Lança IOError se o arquivo não existir ou não puder ser lido.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_file_content(file_path: str, content: str) -> None:
        """
        Escreve 'content' em 'file_path', criando pastas se necessário.

        Exemplo:
          FileManager.write_file_content("out/relatorio.txt", "texto")
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
