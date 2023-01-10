import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 11')
class Testproject_11_1(WebBase):

    @allure.title('Смок 11_1 Подборка все акционные товары проверка авторизованным пользователем)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_11_1(self):
        project = self.APP.web_activity.button_to_project_11()
        self.APP.web_steps.step_test_11_1()
        #project = self.APP.web_activity.button_to_project()
        self.APP.web_any_page.close_cookie()
        project.click_btn_registration()
        project.click_phone()
        txt_phone = "9883237989"
        project.send_phone(txt_phone)
        project.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        project.small_wait()
        city = "Санкт-Петербург и ЛО"
        sw = "1"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        project.select_address_self_any(address_market, city, sw)
        project.small_wait()

        project = self.APP.web_activity.button_to_project_11()
        project.check_items()
        project.sort_items()
        project.send_range_left()
        project.send_range_right()
        project.sort_brand()
        project.sort_noda()




