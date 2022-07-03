
import chromedriver_binary
import allure
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

    def get_url_by_link(self, link):
        driver = self.driver
        driver.get(link)
        try:
            WebDriverWait(driver, 10).until(
                lambda drive: driver.execute_script('return document.readyState') == 'complete')
            return driver.current_url
        except WebDriverException:
            with allure.tag("link not worked"):
                return f"{driver.current_url} IS NOT REACHABLE"

    def destroy(self):
        self.driver.quit()
