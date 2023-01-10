import time
from random import random
import allure
import pytest
import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 15')
class Testproject_15(WebBase):

    @allure.title('Смок 15 Избранное товары, списки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_15(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_15()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_15)
        project.click_favorites_small()
        project.click_favorites_small()
        project.click_favorites_small()
        project.basket_add_small()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_15_1)
        project.click_favorites_remove()
        project.add_basket()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_15_2)
        v = "Список"
        project.click_tab_tab(v)
        project.click_manual_send()
        vv = "cok"
        project.send_manual_send(vv)
        project.send_enter_now()
        vvv = "Кола"
        project.send_manual_send(vvv)
        project.send_enter_now()
        n = 4
        project.click_button_delete(n)
        project.click_button_repair()
        m = 3
        project.click_button_delete(m)
        #assert n == m , "Нет страницы поиска "







