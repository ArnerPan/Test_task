
from model import Data_collector as Collector
from selenium.webdriver.common.by import By
import pytest
import allure
import requests

links = Collector.get_links_from("https://www.mos.ru/")


@allure.link("https://t.me/ArnerPan", name="author")
@allure.sub_suite("Check header and footer presence")
@allure.description("Checking if header is present and visible")
@allure.story("check presence of header")
def test_header(should, method=By.CSS_SELECTOR, selector: str = ".Header_inside__1MzA3 "):
    with allure.step(f"wait until -> {selector} is displayed "):
        should.open_mos_page()
        should.element_visible(method, selector,)


@allure.link("https://t.me/ArnerPan", name="author")
@allure.sub_suite("Check header and footer presence")
@allure.description("Checking if footer is present and visible")
@allure.story("check presence of footer")
def test_footer(should, method=By.CSS_SELECTOR, selector: str = ".Footer_footer__3tfqc"):
    with allure.step(f"wait until -> {selector} is displayed "):
        should.open_mos_page()
        should.element_visible(method, selector,)


@allure.link("https://t.me/ArnerPan", name="author")
@allure.sub_suite("Collect links and check on 200 status ")
@allure.description("Get all links on a site , check every link on <200> response code")
@allure.story("test every site link on 200 status")
@pytest.mark.parametrize('link', links)
def test_response(link):
    response_code = requests.head(link).status_code
    with allure.step(f"site responded with{response_code}  code"):
        assert response_code == 200, f"got {response_code} instead"


@allure.link("https://t.me/ArnerPan", name="author")
@allure.sub_suite("Check links amount")
@allure.description("check amount of links is 280")
@allure.story("check amount of links")
def test_links_amount(amount: int = 280):
    with allure.step(f"got links {len(links)} of {amount}"):
        assert len(links) == amount


@allure.link("https://t.me/ArnerPan", name="author")
@allure.sub_suite("Get all links on a site, check if they direct exact to address")
@allure.description("Check if link follows exactly to it`s URL")
@allure.story("check every link is direct to address ")
@pytest.mark.parametrize('link', links)
def test_link_is_direct_to_address(should, link):
    with allure.step(f"Got URL {should.get_url_by_link(link)} by link {link} "):
        assert should.get_url_by_link(link) == link, "URL IS DIFFERENT"
