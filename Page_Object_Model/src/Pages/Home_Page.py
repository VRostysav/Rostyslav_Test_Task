from Page_Object_Model.src.Base_Page import SeleniumExtended
from Page_Object_Model.src.Helpers.config_helpers import add_base_url
from Page_Object_Model.src.Pages.Locators.Insider_Home_Page_Locators import HomePageLocators


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        homepage = add_base_url()
        self.driver.get(homepage)

    def get_home_page_title(self):
        home_page_title = self.sl. wait_end_get_element_text(self.MAIN_HEADING)
        nice_text = ''.join(home_page_title.splitlines())
        return nice_text

    def click_company_in_navigation_bar(self):
        self.sl.wait_and_click(self.COMPANY_MENU)

    def select_career_option(self):
        self.sl.wait_and_click(self.CAREERS_OPTION)

    def accept_cookies(self):
        self.sl.wait_and_click(self.COOKIES)


