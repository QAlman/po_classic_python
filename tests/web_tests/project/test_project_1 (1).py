import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 1')
class Testproject_1(WebBase):

    @allure.title('Смок 1 Фильтр по цене')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_1(self):

        project = self.APP.web_activity.button_to_project_1()
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.send_range_left()
        project.send_range_right()
        project.compare_all()


