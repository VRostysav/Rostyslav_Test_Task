from Page_Object_Model.src.Base_Page import SeleniumExtended
from Page_Object_Model.src.Helpers.config_helpers import add_base_url
from Page_Object_Model.src.Pages.Locators.Career_QA_Page_Locators import CareerPageLocators


class CareerPage(CareerPageLocators):
    career_page = 'careers/quality-assurance/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_career_page(self):
        homepage = add_base_url()
        career_url = homepage + self.career_page
        self.driver.get(career_url)

    def accept_cookies(self):
        self.sl.wait_and_click(self.COOKIES)

    def click_all_qa_jobs(self):
        self.sl.wait_and_click(self.SEE_QA_JOB_BUTTON)


