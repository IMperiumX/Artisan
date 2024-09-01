import importlib


class PluginManager:
    def install_plugin(self, plugin_path: str) -> None:
        """Install a new plugin."""
        # Load the plugin module
        plugin_module = importlib.import_module(plugin_path)
        # Check if the module has a function named "register"
        if hasattr(plugin_module, "register"):
            # Call the "register" function
            plugin_module.register()
        else:
            raise AttributeError("Plugin does not have a 'register' function")
