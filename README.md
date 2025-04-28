# Python Toolkit 🛠️🐍

[![PyPI Version](https://img.shields.io/pypi/v/bertho-toolkit.svg)](https://pypi.org/project/bertho-toolkit/) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/bertho-toolkit)](https://pypi.org/project/bertho-toolkit/)

Welcome to **Python Toolkit**, a lightweight and personal collection of utilities crafted to make everyday development tasks easier, faster, and more elegant. ✨

This project was born from the need to reuse reliable patterns across different Python applications — instead of rewriting the same helpers every time, now everything is centralized, simple to maintain, and ready to install as a package. 🚀

Whether you are managing environment variables, automating file operations, or printing colorful terminal logs, this toolkit makes it clean, fast, and fun. 💬📦

## Installation 📥

Install directly from PyPI:

```bash
pip install bertho-toolkit
```

## Classes Included

### TerminalLogger 🎨🖥️

A simple logger to print colored messages on the terminal for better readability and debugging.

#### Features:
- Success, error, warning, informational, and internal messages.
- Customizable internal logging.

#### Usage:
```python
from bertho_toolkit.terminal_logger import TerminalLogger

logger = TerminalLogger(enable_internal_log=True)
logger.log_success("Operation successful!")
logger.log_error("An error occurred.")
logger.log_warning("Warning issued.", reason="Validation")
logger.log_info("Information message.")
logger.log_internal("Internal debugging info.")
```

### FileManager 📂📝

Manages file-related operations, including file search, read, and write, with environment-based configurations.

#### Features:
- Automatic management of project paths.
- Recursive file search ignoring specified files.
- Robust file read/write operations with automatic directory creation.

#### Usage:
```python
from bertho_toolkit.file_manager import FileManager

fm = FileManager(env_key="CLASS", enable_log=True)
files = fm.get_files_in_search_path("data")
content = fm.read_file_content(files[0])
fm.write_file_content("output/result.txt", content)
```

### EnvManager 🌿🔧

Automatically handles loading and managing environment variables from a `.env` file.

#### Features:
- Automatic `.env` file discovery.
- CRUD operations on environment variables.
- Utility methods for handling prefixed environment variables.

#### Usage:
```python
from bertho_toolkit.env_manager import EnvManager

env = EnvManager(enable_log=True)
api_key = env.get("API_KEY")
env.set("NEW_VAR", "value")
env.remove("OLD_VAR")
folder_path = env.get_folder("data")
```

## Contributing 🤝

Feel free to open issues or submit pull requests to improve this toolkit. Contributions are always welcome!

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

