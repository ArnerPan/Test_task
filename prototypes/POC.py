#1) Перейти на страницу https://www.mos.ru/
#2) Проверить наличие шапки подвала.
#3) Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)
#4) Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка

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

driver = webdriver.Chrome()

n = 0
i = 0
link_list = []
wait = WebDriverWait(driver, 10)


driver.get('https://www.mos.ru/')
header = "#mos-header > div.Header_header__1FD6w.Header_headerRendered__24O7k > div"
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, header)))










print("header is visible")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#mos_footer > footer")))
print("footer is visible")

founded_links = driver.find_elements(By.CSS_SELECTOR, ":link")
for link_element in founded_links:
    link_url = link_element.get_attribute("href")
    driver.switch_to.new_window('tab')
    wait.until(ec.number_of_windows_to_be(2))
    try:
      driver.get(link_url)
      time.sleep(4)
      if driver.current_url == link_url:
          is_direct = "YES"
      else:
          is_direct = "NO"
    except WebDriverException:
      is_direct = "NOT_REACHABLE"

    driver.close()
    status_code = requests.head(link_url)
    link_list.append((link_url, is_direct, status_code))
    i = i+1
    print(link_list[-1], "№", i)
    driver.switch_to.window(driver.window_handles[0])
    assert len(driver.window_handles) == 1
    n = n+1

print("there is ", n, "links")
driver.close()
