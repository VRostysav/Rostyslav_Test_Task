from Page_Object_Model.src.Base_Page import SeleniumExtended
from Page_Object_Model.src.Helpers.config_helpers import add_base_url
from Page_Object_Model.src.Pages.Locators.Lever_Page_Locators import LeverPageLocators


class LeverPage(LeverPageLocators):
    lever_page = 'https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_lever_page(self):
        self.driver.get(self.lever_page)

    def get_home_page_title(self):
        home_page_title = self.sl.wait_end_get_element_text(self.JOB_DESCRIPTION)
        return home_page_title
