from data.GroupData import GroupData
from data.Settings import Settings
from engine.API.Tickets.api_requests import ApiRequests
from engine.API.APIBase import APIBase
from engine.DriverInstance import DriverInstance
from engine.WEB.AnyPage import AnyPage
from engine.WEB.activity import Activity
from engine.WEB.ecom.ecom_test import ecom_create
from engine.WEB.ecom.ecom_steps import ecom_steps



class ApplicationManager:

    group_data = GroupData()
    settings = Settings()

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.api_base = APIBase(self)
        self.api_requests = ApiRequests(self)
        self.web_any_page = AnyPage(self)
        self.web_activity = Activity(self)
        self.web_ecom = ecom_create(self)
        self.web_steps = ecom_steps(self)

