import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 34')
class Testproject_34(WebBase):

    @allure.title('Смок 34 Создание заказа с примененным промокодом на доставку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_34(self):

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
        pr = "Тест11"
        project.add_promocode(pr)
        p = project.get_price()
        z = " 10%"
        project.click_apply(z)
        pt = project.get_price_tips()
        pf = project.get_price_final()
        project.continue_next()
        d = 100
        project.check_price(p, pf, d)
        project.check_price_basket(pf)
        project.select_flat()
        project.click_delivery()
        project.click_other_card()
        project.select_card()
        project.send_pay()
        project.click_success()
        project.final_table()
        project.check_final(pf)


