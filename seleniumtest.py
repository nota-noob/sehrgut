from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.binary_location = "/usr/bin/firefox"
service = Service(executable_path ="/home/opc/bot_py/.venv/WebDriverManager/gecko/v0.35.0/geckodriver-v0.35.0-linux64/geckodriver")
driver = webdriver.Firefox(options=options,service=service)
driver.get("https://florr.io/")
driver.implicitly_wait(2)
print(driver.page_source)