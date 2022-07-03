import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


def get_links_from(url: str = "https://www.mos.ru/", avoid_duplicate: bool = False):
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_step: int = last_height/100
    scroll: int = 0
    while scroll < last_height:
        scroll = scroll + scroll_step
        driver.execute_script(f"window.scrollTo(0, {scroll})")
        time.sleep(0.01)
    founded_links = driver.find_elements_by_css_selector(":link")
    if avoid_duplicate is True:
        links = []
        for link_element in founded_links:
            if link_element.get_attribute("href") not in links:
                links.append(link_element.get_attribute("href"))

    else:
        links = ['{}'.format(link_element.get_attribute("href"))
                 for link_element in founded_links]

    driver.close()
    return links
