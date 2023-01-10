import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 6')
class Testproject_6(WebBase):

    @allure.title('Смок 6 Сортировка в нодах каталога')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_6(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_6()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        project.open_noda_coffee()
        project.sort_items_pop()
        item = "Кофе зерновой EGOISTE Noir, 1кг"
        project.get_items_one(item)
        project.sort_items()






