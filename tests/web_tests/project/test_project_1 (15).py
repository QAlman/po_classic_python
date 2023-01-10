import time
from random import random
import allure
import pytest
import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 14')
class Testproject_14(WebBase):

    @allure.title('Смок 14 Отзывы,комментарии,шаринг')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_14(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_14()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        sw = "2"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        city = "Санкт-Петербург и ЛО"
        project.select_address_self_any(address_market, city, sw)
        #time.sleep(4)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_14_1)
        project.get_rating()
        project.click_feedback()
        project.get_feed_rating()
        project.get_feed_comment()
        project.page_up_local()
        project.click_share()
        project.click_favorites_item()
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_14)
        project.click_share_favorites()
        z = "Отправить список"
        project.check_share_send(z)
        o = "Ссылка"
        project.click_share_link(o)
        v = "Список"
        project.click_tab_tab(v)
        project.click_manual_send()
        vv = "картофель"
        project.send_manual_send(vv)
        project.send_enter_now()
        vvv = "макароны"
        project.send_manual_send(vvv)
        project.send_enter_now()
        project.click_share_favorites()
        z = "Отправить список"
        project.check_share_send(z)
        o = "Ссылка"
        project.click_share_link(o)







