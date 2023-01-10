import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 31')
class Testproject_31_1(WebBase):

    @allure.title('Смок 31_1 Страница бренда авторизованный ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_31_1(self):
        project = self.APP.web_activity.button_to_project()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        self.APP.web_steps.step_test_31()
        #project.click_btn_registration()
        project.click_phone()
        txt_phone = "9945274140"
        project.send_phone(txt_phone)
        project.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        project.small_wait()
        city = "Санкт-Петербург и ЛО"
        sw = "1"
        address_market = "ш. Выборгское, д. 11, лит. А"
        project.select_address_self_any(address_market, city, sw)
        # project.select_address(address_market)
        project.open_catalog()
        project.open_noda_coffee()
        project.select_tee()
        project.move_to_brand()
        project.select_brand()
        b = "Страница RICHARD"
        project.page_brand(b)
        project.go_to_brand()
        project.page_brand(b)

