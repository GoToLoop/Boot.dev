from collections.abc import Callable

PluginConfig = dict[str, str | None]
PluginFunc = Callable[..., PluginConfig]

# Don't touch above this line

def configure_plugin_decorator(func: PluginFunc) -> PluginFunc:
    return lambda *args: func(**dict(args))
