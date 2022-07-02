import time
from .web_driver_interface import WebDriverInterface
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver(WebDriverInterface):

    chrome_path = 'C:\Program Files (x86)\chromedriver.exe'
    game_url = 'https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/'
    user_name = 'orkeren8@gmail.com'
    password = 'Orkeren8!'

    def __init__(self):
        self.driver = None

    def open_page(self):
        """open the main page of the game

        :return: None
        """
        options = webdriver.ChromeOptions()  # create options var
        options.add_experimental_option("detach", True)  # make chrome to not close
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # install required chrome
        # driver with desired options
        self.driver.get(self.game_url)
        self.login()

    def login(self):
        user_name = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, 'password')

        user_name.send_keys(self.user_name)
        password.send_keys(self.password)

        self.driver.find_element(By.NAME, 'login').click()













