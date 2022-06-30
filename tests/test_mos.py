# 1) Перейти на страницу https://www.mos.ru/
# 2) Проверить наличие шапки подвала.
# 3) Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)
# 4) Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка
import allure
import requests
import pytest
import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


def test_some():
    print("blep")
    driver = webdriver.Chrome()


def test_header_is_visible():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(('https://www.mos.ru/'))

    header = "#mos-header > div.Header_header__1FD6w.Header_headerRendered__24O7k > div"
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, header)))


@pytest.mark.xfail()
def test_header_is_invisible_fpass():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.mos.ru/')
    header = "#mos-header > div.Header_header__1FD6w.Header_headerRendered__24O7k > div"
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, header)))


def test_footer_is_visible():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#mos_footer > footer")))


@pytest.mark.xfail()
def test_footer_is_invisible_xfail():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "#mos_footer > footer")))


def get_links():
    driver = webdriver.Chrome()
    driver.get('https://www.mos.ru/')
    founded_links = driver.find_elements(By.CSS_SELECTOR, ":link")

    links = ['{}'.format(link_element.get_attribute("href"))
             for link_element in founded_links]
    return links


@allure.step("проверяем ссылки!")
@pytest.mark.parametrize('link', get_links())
def test_response_code_200(link):
    response_code = requests.head(link).status_code
    with allure.story(f'site responded with {response_code} code'):
        assert response_code == 200






