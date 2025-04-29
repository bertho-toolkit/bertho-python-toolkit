
# TerminalLogger 🎨

**TerminalLogger** provides a simple way to print colored logs in your terminal.

## Features

- Success (Green)
- Error (Red)
- Warning (Yellow)
- Info (Cyan)
- Internal Logs (Gray)

## Example

```python
from bertho_toolkit.terminal_logger import TerminalLogger

logger = TerminalLogger(enable_internal_log=True)
logger.log_success("Success message!")
logger.log_error("Error message!")
logger.log_warning("Warning message!")
logger.log_info("Info message!")
logger.log_internal("Internal debug message")
```
