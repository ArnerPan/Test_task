
import chromedriver_binary
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as ec


class App:

    def __init__(self, driver):
        self.driver = driver

    def open_mos_page(self):
        driver = self.driver
        driver.get("https://www.mos.ru/")

    def element_visible(self, method, locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((method, locator)))

    def get_all_links_from_url(self, url: str):

        chrome_options = Options()
        chrome_options.headless = True
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        founded_links = self.driver.find_elements_by_css_selector(":link")
        links = ['{}'.format(link_element.get_attribute("href"))
                 for link_element in founded_links]
        driver.close()
        return links

    def get_url_by_link(self, link):

        driver = self.driver
        driver.get(link)
        try:
            return driver.current_url
        except WebDriverException:
            with allure.tag("link not worked"):
                return f"{driver.current_url} IS NOT REACHABLE"

    def destroy(self):
        self.driver.quit()
