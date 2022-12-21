import allure
import requests

from engine.API.APIBase import APIBase


class Token(APIBase):

    @allure.step('Получение токена для пользователя {user_name}. get_token')
    def get_token(self, user_name= f'{USER}'):

        # url = self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['AUTH_URL']
        # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # body = {
        #     'grant_type': 'client_credentials',
        #     'client_id': self.manager.settings.GLOBAL[self.manager.settings.branch]['USERS'][user_name]['User_id'],
        #     'client_secret': self.manager.settings.GLOBAL[self.manager.settings.branch]['USERS'][user_name]['client_secret'],
        # }
        # response = requests.post(url, headers=headers, data=body)
        #
        # self.manager.group_data.response = response
        # response = response.json()
        # self.manager.group_data.access_token = response['access_token']
        # self.manager.group_data.expires_in = response['expires_in']
        # self.manager.group_data.token_type = response['token_type']
