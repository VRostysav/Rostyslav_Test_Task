from Page_Object_Model.src.Base_Page import SeleniumExtended
from Page_Object_Model.src.Helpers.config_helpers import add_base_url
from Page_Object_Model.src.Pages.Locators.General_Career_Page_Locators import CareerPageLocators


class GeneralCareerPage(CareerPageLocators):
    general_career_page = 'careers/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_general_career_page(self):
        homepage = add_base_url()
        career_page_url = homepage + self.general_career_page
        self.driver.get(career_page_url)

    def get_page_title_text(self):
        page_title = self.sl.wait_end_get_element_text(self.PAGE_TITLE)
        return page_title
