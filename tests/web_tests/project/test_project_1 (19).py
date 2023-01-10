import time
from random import random
import allure
import pytest

import engine.WEB.project.project_test
from Test.web_tests.WebBase import WebBase


@allure.feature('Web - project')
@allure.story('Смок № 21')
class Testproject_21_1(WebBase):

    @allure.title('Смок 21_1 Рецепты (авторизованный/неавторизованный) - авторизованный ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_project_21_1(self):

        project = self.APP.web_activity.button_to_project()
        self.APP.web_steps.step_test_21()
        #self.APP.web_any_page.close_citypiker()
        self.APP.web_any_page.close_cookie()
        project.click_phone()
        num = "9574130558"
        project.send_phone(num)
        project.click_next_button()
        #project.popup_close_reg()
        arg = [0]
        self.APP.web_any_page.send_sms_code_phone(*arg)
        project.small_wait()
        project.favorites_move()
        project.favorites_receipts()
        project.clear_favorites_receipt()
        # #project.popup_close_reg()
        city = "Санкт-Петербург и ЛО"
        sw = "1"
        address_market = "ул.  Савушкина, д. 112, лит. А"
        project.select_address_self_any(address_market, city, sw)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_21)
        br = "Рецепты"
        ba = "Статьи"
        bv = "Видео"
        bf = "Избранное"
        project.check_view_block(br)
        project.check_view_block(ba)
        project.check_view_block(bv)
        project.check_view_block(bf)
        project.check_view_selections()
        cr = "Рецепты|Все категории"
        project.clic_all_categories(cr)
        project.clic_add_favotites()
        project.clic_receipt_cart()
        iz = "В избранном"
        project.check_receipt_cart(iz)
        project.click_receipt_cart_favorites()
        iz = "В избранное"
        project.check_receipt_cart(iz)
        project.click_receipt_cart_offer()
        project.check_receipt_cart_vk_f()
        project.page_down_local()
        #time.sleep(22222)
        igr1 = "Вода без газа"
        igr2 = "Сливки (40%)"
        project.click_receipt_cart_ingredients(igr1, igr2)
        project.clic_add_cart_one()
        iz3 = "Перейти в избранное"
        project.check_add_cart_one(iz3)
        tag = "Весь год"
        project.clic_tag_item(tag)
        ur = engine.WEB.project.project_test.Locator.project_url_21_1
        project.check_url_receipt(ur)
        tag_2 = "весь год"
        project.check_receipt_cart_checkbox(tag_2)
        tag_3 = "бобовые"
        itm = project.get_receipt_tag_tree(tag_3)
        project.click_receipt_cart_ingredient_one(tag_3)
        project.check_receipt_cart_item(itm)
        project.page_down_local()
        project.click_clear_item()
        project.page_up_local()
        av = "авокадо"
        project.send_receipt_item(av)
        project.page_up_local()
        project.click_receipt_cart_ingredient_one(av)
        # блок с ингридиентами
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_21)
        cv = "Видео|Показать все"
        project.clic_all_categories(cv)
        tl = "Рецепты с видео"
        project.check_view_all_title(tl)
        mc = "Новый год"
        project.click_receipt_cart_ingredient_one(mc)
        #блок работы с рецептами видео
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_21)
        cta = "Смотреть все|Блюда с ягодами и фруктами"
        project.clic_all_categories(cta)
        tls = "Блюда с ягодами и фруктами"
        project.check_view_all_title(tls)
        project.open_page_all(engine.WEB.project.project_test.Locator.project_url_21)
        en = "Лосось (филе)"
        project.click_receipt_ingredient_one(en)
        tlsl = "Каталог рецептов: лосось (филе)"
        project.check_view_all_title(tlsl)
        itl = "2"
        #project.check_receipt_cart_item(itl)

