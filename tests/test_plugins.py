from python import Plugin, register, get


class DemoPlugin(Plugin):

    name = "demo"

    def run(self):
        return "OK"


def test_plugin():

    plugin = DemoPlugin()

    register(plugin)

    assert get("demo").run() == "OK"
