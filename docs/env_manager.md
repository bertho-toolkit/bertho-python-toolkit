
# EnvManager 🌱

**EnvManager** is a utility to manage environment variables easily from `.env` files.

## Features

- Auto-locate `.env` files
- Load variables into a dictionary
- Get, set, remove, and save variables

## Example

```python
from bertho_toolkit.env_manager import EnvManager

env = EnvManager(enable_log=True)
api_key = env.get("API_KEY")
env.set("NEW_VAR", "value")
env.remove("OLD_VAR")
```
