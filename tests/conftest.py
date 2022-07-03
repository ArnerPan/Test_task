import pytest
import chromedriver_binary
from selenium import webdriver
from model.Appliccation import App
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def should():
    headless = "true"
    chrome_options = Options()
    if headless == "true":
        # Set headless flag to true
        chrome_options.headless = True
    else:
        chrome_options.headless = False

    # Initiate Chrome
    driver = webdriver.Chrome(chrome_options=chrome_options)

    app = App(driver)

    yield app
    app.destroy()


