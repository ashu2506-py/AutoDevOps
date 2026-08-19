class PluginRegistry:

    def __init__(self):

        self._plugins = {}

    def register(self, plugin):

        self._plugins[plugin.name] = plugin

    def get(self, name):

        return self._plugins.get(name)

    def all(self):

        return list(
            self._plugins.values()
        )

    def names(self):

        return list(
            self._plugins.keys()
        )