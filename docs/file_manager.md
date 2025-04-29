
# FileManager 📂

**FileManager** simplifies file search, reading, and writing based on environment paths.

## Features

- Search files recursively
- Ignore predefined files
- Read/write file contents safely

## Example

```python
from bertho_toolkit.file_manager import FileManager

fm = FileManager(env_key="CLASS", enable_log=True)
files = fm.get_files_in_search_path("data")
content = fm.read_file_content(files[0])
fm.write_file_content("output/result.txt", content)
```
