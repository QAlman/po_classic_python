import time
from random import random
import allure
import pytest
import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 12')
class Testproject_12(WebBase):

    @allure.title('Смок 12 Наличие в других ТК')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_12(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_12()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А" #ул.  Савушкина, д. 112, лит. А
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        #time.sleep(4)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_12)
        address = "ул. Савушкина, д. 112, лит. А"
        project.check_container(address)
        project.click_container_address()
        project.click_container_search()
        address = "выборгское, д. 11"
        project.send_container_search(address)
        stock = "Товара много"
        project.check_container_search_address(stock)
        address = "ш. Выборгское, д. 11, лит. А"
        project.click_container_search_address(address)
        project.page_up_local()
        z = project.check_address_location()
        assert address in z, "We have problem"

        sw = "1"
        address_market = "ш. Кирилловское, д. 50А"
        city = "Кострома"
        project.select_address_self_any(address_market, city, sw)






