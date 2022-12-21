import time
import allure

from selenium.webdriver.common.by import By
from engine.WEB.AnyPage import AnyPage


class Locator:

    activity_subheader = (By.XPATH, '//div[@class="activity-subheader"]')
    button_folder_create = (By.XPATH, "//*[text()='Создать папку']")  # -- my
    sandwich = (By.XPATH, "//*[@class='sandwich']") # --- my

    ecom_url = "https://stage.lentatest.com/"
    ecom_url_1 = "https://stage.lentatest.com/catalog/kulinariya-i-polufabrikaty-sobstvennogo-proizvodstva/"
    ecom_url_2 = "https://stage.lentatest.com/catalog/napitki"
    ecom_url_11 = "https://stage.lentatest.com/promo/"
    ecom_url_3 = "https://stage.lentatest.com/npl/authentication/"




class Activity(AnyPage):

    def page_loaded(self):
        #self.find_element(Locator.activity_subheader)
        pass

    @allure.step('Работа c URL ECOM')
    def button_to_ecom(self):
        # Переходим на целевую страницу теста
        self.goto_page(Locator.ecom_url_3)
        time.sleep(3)
        return self.manager.web_ecom


    @allure.step('Работа c URL ECOM - тест 1')
    def button_to_ecom_1(self):
        # Переходим на целевую страницу теста
        self.goto_page(Locator.ecom_url_1)
        time.sleep(3)
        return self.manager.web_ecom

    @allure.step('Работа c URL ECOM - тест 2')
    def button_to_ecom_2(self):
        # Переходим на целевую страницу теста
        self.goto_page(Locator.ecom_url_2)
        time.sleep(3)
        return self.manager.web_ecom

    @allure.step('Работа c URL ECOM - тест 11')
    def button_to_ecom_11(self):
        # Переходим на целевую страницу теста
        self.goto_page(Locator.ecom_url_11)
        time.sleep(3)
        return self.manager.web_ecom







