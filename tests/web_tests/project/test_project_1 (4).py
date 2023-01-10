import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 4')
class Testproject_4(WebBase):

    @allure.title('Смок 4 Акции , выпадающее меню')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_4(self):
        project = self.APP.web_activity.button_to_project()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.move_to_actions()
        z = "Акции для спб"
        project.select_actions(z)


