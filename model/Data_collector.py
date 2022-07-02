
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


def get_links_from(url: str):
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    founded_links = driver.find_elements_by_css_selector(":link")
    links = ['{}'.format(link_element.get_attribute("href"))
             for link_element in founded_links]
    driver.close()
    return links




