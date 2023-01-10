import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 19')
class Testproject_19(WebBase):

    @allure.title('Смок 19 Товар закончился, выбрать другой')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_19(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_19
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        city = "Санкт-Петербург и ЛО"
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        project.select_address_self_any(address_market, city, sw)
        project.open_catalog()
        project.open_noda_coffee()
        project.select_tee()
        project.basket_add()
        project.basket_move()
        city = "Санкт-Петербург и ЛО"
        sw = "1"
        address_market = "Малый пр. ВО, д. 54, лит"
        project.select_address_self_any(address_market, city, sw)
        # address_market = "г. Ломоносов, ул. Михайловская, д. 40/7"
        c = "Товар закончился"
        project.basket_check_delivery(c)
        project.click_next_item()
        project.switch_to_new_tab()
        project.check_noda_black_tee()







