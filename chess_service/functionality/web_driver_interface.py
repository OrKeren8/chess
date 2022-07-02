from abc import ABC, abstractmethod

class WebDriverInterface(ABC):

    @abstractmethod
    def open_page(self):
        """open the main page of the game

        return: None
        """
        raise NotImplementedError

    @abstractmethod
    def login(self):
        """login into the game

        return: None, raised corresponding error
        """
        raise NotImplementedError

    @abstractmethod
    def play_vs_pc(self):
        """play a game against a pc

        return: None, corresponding error
        """
        raise NotImplementedError
