"""
Módulo terminal_logger
----------------------

Fornece a classe TerminalLogger para registrar mensagens coloridas no terminal:

  - LogSuccess: exibe mensagem de sucesso (verde).
  - LogError: exibe mensagem de erro (vermelho).
  - LogWarning: exibe aviso (amarelo), opcionalmente com motivo.
  - LogInternal: exibe log interno (cinza) quando habilitado.
  - LogInformation: exibe mensagem informativa (ciano).
"""
from typing import Optional


class TerminalLogger:
    """
    Logger de terminal com suporte a cores ANSI.

    Parâmetros:
      internal_log (bool): se True, exibe mensagens internas via LogInternal.

    Atributos de cor (ANSI):
      GREEN, RED, YELLOW, CIANO, CINZA, WHITE, RESET
    """
    GREEN: str = "\033[92m"
    RED: str = "\033[91m"
    YELLOW: str = "\033[93m"
    CIANO: str = "\033[96m"
    CINZA: str = "\033[90m"
    WHITE: str = "\033[97m"
    RESET: str = "\033[0m"

    def __init__(self, internal_log: bool = True) -> None:
        self._internal_log = internal_log

    def LogSuccess(self, message: str) -> None:
        """
        Exibe uma mensagem de SUCESSO em verde.
        """
        print(f"{self.GREEN}{message}{self.RESET}")

    def LogError(self, message: str) -> None:
        """
        Exibe uma mensagem de ERRO em vermelho.
        """
        print(f"{self.RED}{message}{self.RESET}")

    def LogWarning(self, message: str, reason: Optional[str] = None) -> None:
        """
        Exibe um AVISO em amarelo, com motivo opcional.

        Parâmetros:
          message (str): texto do aviso.
          reason  (str): contexto ou motivo, será mostrado entre colchetes.
        """
        prefix = f"[ {reason} ] - " if reason else ""
        print(f"{prefix}{self.YELLOW}{message}{self.RESET}")

    def LogInternal(self, message: str, overwrite_show_log: bool = False) -> None:
        """
        Exibe uma mensagem de log interno em cinza se internal_log=True.

        Parâmetros:
          message             (str): texto do log.
          overwrite_show_log (bool): força a exibição mesmo que internal_log=False.
        """
        if overwrite_show_log or self._internal_log:
            print(f"{self.CINZA}{message}{self.RESET}")

    def LogInformation(self, message: str) -> None:
        """
        Exibe uma mensagem de INFORMAÇÃO em ciano.
        """
        print(f"{self.CIANO}{message}{self.RESET}")
