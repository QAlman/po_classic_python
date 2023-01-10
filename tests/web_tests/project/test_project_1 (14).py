import time
from random import random
import allure
import pytest
import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 13')
class Testproject_13(WebBase):

    @allure.title('Смок 13 Блок "Вы смотрели"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_13(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_13()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        project.open_noda_milk()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13_1)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13_2)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13_3)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13_4)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13_5)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_13_6)
        project.page_down_local()
        project.move_to_carousel()

        project.click_carousel_left()
        project.click_carousel_right()








