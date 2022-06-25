from abc import ABC, abstractmethod

class FuncInterface(ABC):

    @abstractmethod
    def do_something(self):
        raise NotImplementedError
