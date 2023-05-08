This package contains only a class with only one `__init__` which retrieves the requested environment variables.

```python
from tokens import Tokens  # as it all the that the package provides
```

For instance, we've to get some authorization tokens that already defined in the environment to interact with the Discord API and the Telegram API.

```python
tokens = Tokens(["discord", "telegram"])
```

The class "`Tokens`" on initialization will retrieve as attributes these tokens from the environment as "`PACKAGE_DISCORD_TOKEN`" and "`PACKAGE_TELEGRAM_TOKEN`" or just "`DISCORD_TOKEN`" and "`TELEGRAM_TOKEN`" if the `__name__` is undefined.

```python
bot.run(tokens.discord)
```

The attribute "`discord`" should contain a string of the token if it has been in the environment, as the same as for "`telegram`".
