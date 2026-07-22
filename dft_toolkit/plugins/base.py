from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base class for DFT-Toolkit plugins.
    """

    name = "plugin"

    @abstractmethod
    def run(self, *args, **kwargs):
        """Execute plugin."""
        raise NotImplementedError
