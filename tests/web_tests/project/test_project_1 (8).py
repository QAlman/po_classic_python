import time
from random import random
import allure
import pytest
import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 8')
class Testproject_8(WebBase):

    @allure.title('Смок 8 Подборки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_8(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_8()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        time.sleep(4)
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
        project.page_down_local()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_8)
        oo = "Подpобнее"
        project.click_button_all(oo)
        project.click_container_address()

