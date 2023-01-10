import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 3')
class Testproject_3(WebBase):

    @allure.title('Смок 3 Фильтр по бренду и фабрике')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_3(self):
        project = self.APP.web_activity.button_to_project_2()
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.move_to_enterprise()
        b = "365"
        project.select_brand_all(b)
        project.show_next_2()
        project.select_fabric(b)
        project.check_select_brand_all(b)
