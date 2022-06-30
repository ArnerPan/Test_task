import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import chromedriver_binary


def check_header(self):
    driver = webdriver.Chrome()
    driver.get('https://www.mos.ru/')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self._header)))
    driver.close()
    return self


def open():
    driver = webdriver.Chrome()
    driver.get('https://www.mos.ru/')
    return driver


def check_visibility(css_locator: str):
    driver = open()
    displayed_element_to_find(driver, css_locator)
    return


def displayed_element_to_find(driver, css_locator: str):

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, css_locator)))
    return


def get_links():
    driver = open()
    driver.get('https://www.mos.ru/')
    founded_links = driver.find_elements(By.CSS_SELECTOR, ":link")
    links = ['{}'.format(link_element.get_attribute("href"))
             for link_element in founded_links]
    driver.close()
    return links


def current_url_check(link):
    driver = webdriver.Chrome()
    driver.get(link)
    try:
        if driver.current_url == link:
            return "YES"
        else:
            return "NO"
    except WebDriverException:
        with allure.tag("link not worked"):
            return "NOT REACHABLE"

