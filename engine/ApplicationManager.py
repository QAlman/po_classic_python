from data.GroupData import GroupData
from data.Settings import Settings
from engine.API.Tickets.api_requests import ApiRequests
from engine.API.APIBase import APIBase
from engine.DriverInstance import DriverInstance
from engine.WEB.AnyPage import AnyPage
from engine.WEB.activity import Activity
 



class ApplicationManager:

    group_data = GroupData()
    settings = Settings()

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.api_base = APIBase(self)
        self.api_requests = ApiRequests(self)
        self.web_any_page = AnyPage(self)
        self.web_activity = Activity(self)
 

