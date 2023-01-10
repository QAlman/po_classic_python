import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 26')
class Testproject_26(WebBase):

    @allure.title('Смок 26 Товар недоступен для доставки,выбрать другой')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_26(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_26()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        #project.click_btn_registration()
        project.click_phone()
        txt_phone = "9945274140"
        project.send_phone(txt_phone)
        project.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        project.small_wait()
        project.basket_move()
        project.clear_basket()
        city = "Новосибирск" #г. Новосибирск, гусинобродское шоссе 64
        sw = "1"
        address_market = "ш. Гусинобродское, д. 64"
        project.select_address_self_any(address_market, city, sw)
        time.sleep(6)
        project.open_catalog()
        #project.open_noda_alco()
        project.open_noda_forhome()
        #project.select_alco_item()
        project.basket_add()
        project.basket_move()
        # city = "Санкт-Петербург и ЛО"
        #sw = "1"
        address_market = "г Новосибирск, Гусинобродское шоссе, д 64" #г Санкт-Петербург, Выборгское шоссе, д 11 литера А
        project.select_address_delivery_any(address_market, city, sw)
        project. small_wait()
        c = "Товар недоступен для доставки" #овар доступен в других магазинах "project"
        project.basket_check_delivery(c)
        # project.click_next_item()
        # project.switch_to_new_tab()
        # project.check_noda_alco()






