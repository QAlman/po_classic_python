import time
import allure

from selenium.webdriver.common.by import By
from engine.WEB.AnyPage import AnyPage


class Locator:

    activity_subheader = (By.XPATH, '//div[@class="activity-subheader"]')
    button_folder_create = (By.XPATH, "//*[text()='Создать папку']")  # -- my
    sandwich = (By.XPATH, "//*[@class='sandwich']") # --- my

     url = "https:// "
 

class Activity(AnyPage):

    def page_loaded(self):
        #self.find_element(Locator.activity_subheader)
        pass

    @allure.step('Работа c URL  ')
    def button_to(self):
        # Переходим на целевую страницу теста
        self.goto_page(Locator.url_3)
        time.sleep(3)
        return self.manager.web 


   







