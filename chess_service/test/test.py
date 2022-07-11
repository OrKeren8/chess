from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.chess.com/')
