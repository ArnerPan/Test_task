import requests
import pytest
from model import Mo
import allure


def test_footer():
    Mo.check_visibility("#mos_footer > footer")


def test_header():
    Mo.check_visibility("#mos-header > div.Header_header__1FD6w.Header_headerRendered__24O7k > div")


@allure.story("gonna to test respond status!")
@pytest.mark.parametrize('link', Mo.get_links())
def test_response(link):
    response_code = requests.head(link).status_code
    with allure.step(f"site responded with{response_code}  code"):
        assert response_code == 200, f"got {response_code} instead"


@pytest.mark.parametrize('link', Mo.get_links())
def test_current_url_is_link_url(link):
    assert Mo.current_url_check(link) == "YES", "LINK IS NOT DIRECT"










