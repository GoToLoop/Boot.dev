from decorators import PluginConfig, configure_plugin_decorator

@configure_plugin_decorator
def configure_backups(
    path: str = "~/backups", prefix: str = "copy_", extension: str = ".txt"
) -> PluginConfig:
    return {
        "path": path,
        "prefix": prefix,
        "extension": extension,
    }


@configure_plugin_decorator
def configure_login(
    user: str | None = None, password: str | None = None, token: str | None = None
) -> PluginConfig:
    return {
        "user": user,
        "password": password,
        "token": token,
    }
