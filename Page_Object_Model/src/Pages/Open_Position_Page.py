from Page_Object_Model.src.Base_Page import SeleniumExtended
from Page_Object_Model.src.Helpers.config_helpers import add_base_url
from Page_Object_Model.src.Pages.Locators.Open_Positions_Locators import OpenPositionsLocators


class OpenPositionsPage(OpenPositionsLocators):
    career_page = 'careers/open-positions/?department=qualityassurance'

    def __init__(self, driver, parent_handle):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.parent_handle = parent_handle

    def go_to_open_position_page(self):
        homepage = add_base_url()
        career_url = homepage + self.career_page
        self.driver.get(career_url)

    def scroll_to_element(self):
        self.sl.scroll_and_click(self.BROWSE_OPEN_POSITIONS)

    def accept_cookies(self):
        self.sl.wait_and_click(self.COOKIES)

    def click_location_dropdown(self):
        self.sl.wait_and_click(self.LOCATION_DROPDOWN)

    def select_all_option(self):
        self.sl.wait_and_click(self.All_OPTION)

    def first_job_title(self):
        job_title_1 = self.sl.wait_end_get_element_text(self.FIRST_JOB_TITLE)
        return job_title_1

    def second_job_title(self):
        job_title_2 = self.sl.wait_end_get_element_text(self.SECOND_JOB_TITLE)
        return job_title_2

    def third_job_title(self):
        job_title_3 = self.sl.wait_end_get_element_text(self.THIRD_JOB_TITLE)
        return job_title_3

    def check_department(self):
        department = self.sl.wait_end_get_element_text(self.DEPARTMENT_NAME)
        department_text = ''.join(department.splitlines())
        return department_text

    def check_location(self):
        location = self.sl.wait_end_get_element_text(self.LOCATION)
        location_text = ''.join(location.splitlines())
        return location_text

    def move_mouse_to_job_position(self):
        self.sl.move_to_element(self.FIRST_JOB_TITLE)

    def click_view_role_button(self):
        self.sl.wait_and_click(self.VIEW_ROLE_BUTTON)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != self.parent_handle:
                self.driver.switch_to.window(handle)
