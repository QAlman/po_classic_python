import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 10')
class Testproject_10(WebBase):

    @allure.title('Смок 10 Поиск')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_10(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_10()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()

        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)

        project.page_up_local()
        project.click_search_field()
        item ="Молоко"
        project.send_name(item)
        project.click_search_result(item)
        title = project.get_text()
        assert item in title, f"Название {item}не найденно "






