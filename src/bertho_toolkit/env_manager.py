from pathlib import Path
from typing import Dict, Optional
from .terminal_logger import TerminalLogger


class EnvManager:
    """
    Manages environment variables loaded from a '.env' file.

    Attributes:
        env_vars (Dict[str, str]): Dictionary holding environment variables.
        file_path (Path): Path to the '.env' file.

    Args:
        env_path (Optional[str]): Explicit path to the '.env' file. If not provided,
                                  the file is searched automatically.
        enable_log (bool): Enables logging of internal operations. Default is False.
    """

    def __init__(self, env_path: Optional[str] = None, enable_log: bool = False) -> None:
        """
        Initializes the EnvManager and loads environment variables.

        Args:
            env_path (Optional[str]): Path to the '.env' file.
            enable_log (bool): Flag to enable internal logging.
        """
        self.logger = TerminalLogger(enable_log)
        self.env_vars: Dict[str, str] = {}

        self.file_path = Path(env_path) if env_path else self._find_dotenv()
        self.load()

    def _find_dotenv(self) -> Path:
        """
        Automatically searches for a '.env' file starting from the current directory upwards.

        Returns:
            Path: The path to the '.env' file found, or default path if not found.
        """
        current_dir = Path.cwd()
        for parent in [current_dir, *current_dir.parents]:
            dotenv_path = parent / '.env'
            if dotenv_path.exists():
                self.logger.log_internal(f".env file found: {dotenv_path}")
                return dotenv_path
        self.logger.log_warning(".env file not found.")
        return current_dir / '.env'

    def load(self) -> None:
        """
        Loads environment variables from the '.env' file.
        """
        if not self.file_path.exists():
            self.logger.log_warning(f".env file not found at: {self.file_path}")
            return

        with self.file_path.open('r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = map(str.strip, line.split('=', 1))
                        self.env_vars[key] = value
                        self.logger.log_internal(f"Loaded: {key} = {value}")

    def get(self, key: Optional[str], default: Optional[str] = None) -> Optional[str]:
        """
        Retrieves the value of an environment variable.

        Args:
            key (Optional[str]): The key of the variable. Defaults to 'DEFAULT' if None.
            default (Optional[str]): Default value if the key does not exist.

        Returns:
            Optional[str]: The value of the environment variable or default.
        """
        actual_key = key if key is not None else 'DEFAULT'
        return self.env_vars.get(actual_key, default)

    def set(self, key: str, value: str) -> None:
        """
        Sets or updates an environment variable and saves to the '.env' file.

        Args:
            key (str): The key of the variable.
            value (str): The value to set.
        """
        self.env_vars[key] = value
        self.save()

    def remove(self, key: str) -> bool:
        """
        Removes an environment variable.

        Args:
            key (str): The key of the variable to remove.

        Returns:
            bool: True if the variable was removed, False otherwise.
        """
        if key in self.env_vars:
            del self.env_vars[key]
            self.save()
            return True
        return False

    def save(self) -> None:
        """
        Saves all environment variables back to the '.env' file.
        """
        with self.file_path.open('w', encoding='utf-8') as f:
            for key, value in self.env_vars.items():
                f.write(f"{key}={value}\n")

    def get_with_prefix(self, prefix: str, key: Optional[str], default: Optional[str] = None) -> Optional[str]:
        """
        Retrieves an environment variable by combining a prefix and key.

        Args:
            prefix (str): The prefix of the variable.
            key (Optional[str]): The key of the variable. Defaults to 'DEFAULT' if None.
            default (Optional[str]): Default value if the variable is not found.

        Returns:
            Optional[str]: The value of the prefixed environment variable or default.
        """
        actual_key = key if key is not None else 'DEFAULT'
        return self.get(f"{prefix}_{actual_key}", default)

    def get_folder(self, folder_name: str) -> Optional[str]:
        """
        Builds a path to a subdirectory within the specified project path.

        Args:
            folder_name (str): The name of the subdirectory.
        Returns:
            Optional[str]: Full path to the subdirectory or None if the base path is not set.
        """
        default_key = 'DEFAULT_PROJECT_PATH'
        default_project = self.get(default_key)
        return str(Path(default_project) / folder_name) if default_project else None