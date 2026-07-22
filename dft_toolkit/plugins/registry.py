_plugins = {}


def register(plugin):
    _plugins[plugin.name] = plugin


def get(name):
    return _plugins.get(name)


def names():
    return sorted(_plugins.keys())
