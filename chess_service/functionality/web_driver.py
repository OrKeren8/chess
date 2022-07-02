import time
from .web_driver_interface import WebDriverInterface
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver(WebDriverInterface):

    chrome_path = 'C:\Program Files (x86)\chromedriver.exe'

    def __init__(self):
        pass

    @staticmethod
    def install_driver():
        """install required version of chrome for selenium

        :return: driver
        """
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

    def open_page(self):
        """open the main page of the game

        :return: None
        """
        driver = self.install_driver()
        driver.get('https://www.chess.com/')






