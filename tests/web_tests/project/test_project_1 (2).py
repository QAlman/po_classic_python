import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 2')
class Testproject_2(WebBase):

    @allure.title('Смок 2 Сортировка по бренду')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    #@pytest.mark.skip
    def test_project_2(self):
        project = self.APP.web_activity.button_to_project_2()
        self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.move_to_enterprise()
        project.show_next()
        b = "365"
        project.select_brand_all(b)
        project.check_select_brand_all(b)

