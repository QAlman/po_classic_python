import allure
import pytest

import engine.WEB.AnyPage
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Authentication')
class TestApiCreateRequest(ApiBase):

    @allure.title('Authentication by code')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_request_code_a(self):
        #
        request_body = {
                          "card": "string",
                          "code": f"{engine.WEB.AnyPage.Locator.phone_code_api}",
                          "password": "string",
                          "firstName": "string_111",
                          "lastName": "string_asdeq",
                          "dateOfBirth": "2022-08-17T08:31:02.986Z",
                          "phone": f"{engine.WEB.AnyPage.AnyPage.string_d}",
                          "personalDataProcessingAgreed": True,
                          "isMobileApp": True,
                          "hash": "string",
                          "campaignId": "string"
                        }

        r = self.APP.api_requests.post_requests_code(request_body)
        print(r)

