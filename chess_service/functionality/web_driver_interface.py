from abc import ABC, abstractmethod

class WebDriverInterface(ABC):

    @abstractmethod
    def open_page(self):
        """open the main page of the game

        :return: None
        """
        raise NotImplementedError
