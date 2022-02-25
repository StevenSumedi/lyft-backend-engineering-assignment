# ABC = abstract base class
from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

# every child of the serviceable class must include the needs_service method