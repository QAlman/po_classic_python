import time
from random import random
import allure
import pytest
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 5')
class Testproject_5(WebBase):

    @allure.title('Смок 5 Фильтрация по Ноде,Тегу, бренду, производителю')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_5(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_5()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        #project.page_up_local()
        project.open_noda_milk()
        z = "alti"
        project.get_tag_all(z)
        o = project.get_scu_all()
        assert o >= 2, "Карточек больше"
        project.get_tag_all(z)
        v = project.get_scu_all()
        assert v >= 2, "Карточек меньше"
        zz = "Сыр"
        project.select_items_all(zz)
        oo = "Плавленный сыр"
        project.select_items_all(oo)
        vv = "HOCHLAND"
        project.select_brand_all(vv)
        zzz = project.get_scu_all()
        assert zzz >= 8, "Карточек больше"
        ooo = "Хохланд Руссланд"
        project.select_fabric(ooo)
        vvv = project.get_scu_all()
        assert vvv == 2, "Карточек больше"








