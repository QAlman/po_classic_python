import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 34')
class Testproject_34_1(WebBase):

    @allure.title('Смок 34_1 Создание заказа с примененным промокодом (40%) на доставку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip
    def test_project_34_1(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_34()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.click_phone()
        num = "9407718110"
        project.send_phone(num)
        project.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        project.small_wait()
        project.basket_move()
        project.clear_basket()
        sw = "1"
        address_market = "г Новосибирск, Гусинобродское шоссе, д 64"
        city = "Новосибирск"
        project.select_address_delivery_any(address_market, city, sw)
        project.add_basket()
        pr = "Тест12"
        project.add_promocode(pr)
        p = project.get_price()
        z = " 40%"
        project.click_apply(z)
        pt = project.get_price_tips()
        pb = project.get_price()
        project.continue_next()
        project.check_price_40(p)
        project.check_price_basket(pb)
        project.select_flat()
        project.click_delivery()
        project.click_other_card()
        project.select_card()
        project.send_pay()
        project.click_success()
        project.final_table()
        project.check_final(p)


