import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 31')
class Testproject_31(WebBase):

    @allure.title('Смок 31 Страница бренда неавторизованный ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_31(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_31()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()

        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ш. Выборгское, д. 11, лит. А"
        project.select_address_self_any(address_market, city, sw)
        project.open_catalog()
        project.open_noda_coffee()
        project.select_tee()
        project.move_to_brand()
        project.select_brand()
        b = "Страница RICHARD"
        project.page_brand(b)
        project.go_to_brand()
        project.page_brand(b)



