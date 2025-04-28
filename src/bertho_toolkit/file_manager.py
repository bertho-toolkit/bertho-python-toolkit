from pathlib import Path
from typing import List, Optional
from .env_manager import EnvManager
from .terminal_logger import TerminalLogger

IGNORED_FILES = {
    '.env', 'local.env', 'env.example',
    '.DS_Store', 'Thumbs.db', '.gitkeep'
}


class FileManager:
    """
    Manages file operations based on environment variables.

    Attributes:
        PROJECT_PATH (Path): Base project path loaded from environment variables.
        OUTPUT_PATH (Path): Path to output files.
        SEARCH_PATH (Path): Path to search for files.

    Args:
        env_key (str): Prefix key to search for environment variables (e.g., 'CLASS').
        enable_log (bool): Enables logging for operations. Default is True.
    """

    def __init__(self, env_key: str, enable_log: bool = True) -> None:
        """
        Initializes the FileManager by setting paths from environment variables.

        Args:
            env_key (str): Prefix for environment variables.
            enable_log (bool): Flag to enable logging.
        """
        self.env_key = env_key.upper()
        self.logger = TerminalLogger(enable_log)
        env = EnvManager(enable_log=enable_log)

        self.PROJECT_PATH = Path(env.get_with_prefix(
            self.env_key, 'PROJECT_PATH', env.get('DEFAULT_PROJECT_PATH', '.')))
        self.OUTPUT_PATH = Path(env.get_with_prefix(
            self.env_key, 'OUTPUT_PATH', env.get('DEFAULT_OUTPUT_PATH', './output')))
        self.SEARCH_PATH = Path(env.get_with_prefix(
            self.env_key, 'SEARCH_PATH', env.get('DEFAULT_EXTRACTOR_SEARCH_PATH', '.')))

    def get_files_in_search_path(self, append_path: Optional[str] = "") -> List[Path]:
        """
        Retrieves a list of file paths within the search directory, optionally appending a sub-path.

        Args:
            append_path (Optional[str]): Additional subdirectory path to append.

        Returns:
            List[Path]: List of paths found in the search directory, excluding ignored files.
        """
        if not self.SEARCH_PATH.exists():
            self.logger.log_error(f"SEARCH_PATH not found: {self.SEARCH_PATH}")
            return []

        target = self.SEARCH_PATH / append_path
        if not target.exists():
            self.logger.log_warning(f"Path not found: {target}")
            return []

        files_list: List[Path] = []
        for file in target.rglob('*'):
            if file.is_file() and file.name not in IGNORED_FILES:
                files_list.append(file)
        return files_list

    @staticmethod
    def read_file_content(file_path: Path) -> str:
        """
        Reads the content of a file and returns it as a string.

        Args:
            file_path (Path): Path to the file to read.

        Returns:
            str: Content of the file.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            return file_path.read_text(encoding='utf-8')
        except Exception as e:
            raise IOError(f"Could not read file {file_path}: {e}")

    @staticmethod
    def write_file_content(file_path: Path, content: str) -> None:
        """
        Writes content to a file, creating necessary directories.

        Args:
            file_path (Path): Path to the file to write.
            content (str): Content to write into the file.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding='utf-8')
        except Exception as e:
            raise IOError(f"Could not write to file {file_path}: {e}")