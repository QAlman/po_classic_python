import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 11')
class Testproject_11(WebBase):

    @allure.title('Смок 11 Подборка все акционные товары проверка  неавторизованным пользователем)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_11(self):
        project = self.APP.web_activity.button_to_project_11()
        self.APP.web_steps.step_test_11()
        self.APP.web_any_page.close_cookie()
        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        project.select_address_self_any(address_market, city, sw)
        project.page_up_local()
        project.check_items()
        project.sort_items()
        project.send_range_left()
        project.send_range_right()
        project.sort_brand()
        project.sort_noda()




