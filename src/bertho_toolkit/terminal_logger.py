from typing import Optional


class TerminalLogger:
    """
    A utility class for printing colored logs in the terminal.

    Attributes:
        GREEN (str): ANSI code for green color (success messages).
        RED (str): ANSI code for red color (error messages).
        YELLOW (str): ANSI code for yellow color (warning messages).
        CYAN (str): ANSI code for cyan color (informational messages).
        GRAY (str): ANSI code for gray color (internal debug messages).
        WHITE (str): ANSI code for white color.
        RESET (str): ANSI code to reset color.

    Args:
        enable_internal_log (bool): Enables or disables internal debug logs. Default is True.
    """

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    def __init__(self, enable_internal_log: bool = True) -> None:
        """
        Initializes the TerminalLogger.

        Args:
            enable_internal_log (bool): Flag to enable internal log messages.
        """
        self.enable_internal_log = enable_internal_log

    def log_success(self, message: str) -> None:
        """
        Logs a success message in green.

        Args:
            message (str): The success message to display.
        """
        print(f"{self.GREEN}{message}{self.RESET}")

    def log_error(self, message: str) -> None:
        """
        Logs an error message in red.

        Args:
            message (str): The error message to display.
        """
        print(f"{self.RED}{message}{self.RESET}")

    def log_warning(self, message: str, reason: Optional[str] = None) -> None:
        """
        Logs a warning message in yellow, optionally including a reason.

        Args:
            message (str): The warning message to display.
            reason (Optional[str]): An optional reason or context for the warning.
        """
        prefix = f"[ {reason} ] - " if reason else ""
        print(f"{prefix}{self.YELLOW}{message}{self.RESET}")

    def log_internal(self, message: str, force_display: bool = False) -> None:
        """
        Logs an internal debug message in gray if internal logging is enabled.

        Args:
            message (str): The internal message to display.
            force_display (bool): Forces the message to be displayed regardless of settings.
        """
        if self.enable_internal_log or force_display:
            print(f"{self.GRAY}{message}{self.RESET}")

    def log_info(self, message: str) -> None:
        """
        Logs an informational message in cyan.

        Args:
            message (str): The informational message to display.
        """
        print(f"{self.CYAN}{message}{self.RESET}")
