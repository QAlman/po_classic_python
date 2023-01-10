import time
from random import random
import allure
import pytest
import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 9')
class Testproject_9(WebBase):

    @allure.title('Смок 9 Корзина, чекаут, спасибо за заказ Самовывоз (Тест не доделан полсностью)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_9(self):
        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_9()
        # self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.click_phone()
        num = "9407718110"
        project.send_phone(num)
        project.click_next_button()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        time.sleep(4)
        project.refresh()
        sw = "1"
        address_market = "г Новосибирск, Гусинобродское шоссе, д 64"
        city = "Новосибирск"
        project.select_address_self_any(address_market, city, sw)
        project.small_wait()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_9)
        project.small_wait()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_9_1)

        project.page_up_local()
        project.move_to_actions()
        z = "СУПЕРСКИДКИ"
        project.select_actions(z)
        project.move_to_actions()
        z = "Товары недели"
        project.select_actions(z)
        o = "bigmedia карусель"
        project.get_header_title(o)
        project.move_to_carousel()
        project.click_carousel_left()
        project.click_carousel_right()
        project.move_to_actions()
        z = "Подборка Ленточка"
        project.select_actions(z)
        project.move_to_actions()
        z = "landing page"
        project.select_actions(z)
        project.move_to_actions()
        z = "Безумные скидки"
        project.select_actions(z)

