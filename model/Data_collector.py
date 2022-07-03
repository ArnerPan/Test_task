import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


def get_links_from(url: str = "https://www.mos.ru/"):
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll = 1000
    while scroll < last_height:
        scroll = scroll + 1000
        driver.execute_script(f"window.scrollTo(0, {scroll})")
        time.sleep(0.5)

    time.sleep(5)
    founded_links = driver.find_elements_by_css_selector(":link")
    links = ['{}'.format(link_element.get_attribute("href"))
             for link_element in founded_links]
    print(len(links))
    return links











