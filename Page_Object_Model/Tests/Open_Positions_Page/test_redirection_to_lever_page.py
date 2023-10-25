import pytest
from Page_Object_Model.src.Pages.Open_Position_Page import OpenPositionsPage
from Page_Object_Model.src.Pages.Lever_Page import LeverPage


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid14
    def test_jobs_filtered(self):
        open_position_page = OpenPositionsPage(self.driver, self.parent_handle)
        open_position_page.go_to_open_position_page()
        open_position_page.accept_cookies()
        open_position_page.scroll_to_element()
        open_position_page.click_location_dropdown()
        open_position_page.select_all_option()
        leaver_page = LeverPage(self.driver)

        open_position_page.move_mouse_to_job_position()
        open_position_page.click_view_role_button()
        leaver_page.get_home_page_title()
        assert leaver_page.get_home_page_title() == 'Senior Software Quality Assurance Engineer - Remote'

