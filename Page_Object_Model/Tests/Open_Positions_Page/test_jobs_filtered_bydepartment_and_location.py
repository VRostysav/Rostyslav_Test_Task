import pytest
from Page_Object_Model.src.Pages.QA_Career_Page import CareerPage
from Page_Object_Model.src.Pages.Open_Position_Page import OpenPositionsPage


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid13
    def test_jobs_filtered(self):
        career_page = CareerPage(self.driver)
        open_position_page = OpenPositionsPage(self.driver, self.parent_handle)
        career_page.go_to_career_page()
        career_page.accept_cookies()
        career_page.click_all_qa_jobs()
        open_position_page.go_to_open_position_page()
        open_position_page.scroll_to_element()
        open_position_page.click_location_dropdown()
        open_position_page.select_all_option()

        open_position_page.first_job_title()
        assert open_position_page.first_job_title() == 'Senior Software Quality Assurance Engineer - Remote'

        open_position_page.second_job_title()
        assert open_position_page.second_job_title() == 'Software QA Tester- Insider Testinium Tech Hub (Remote)'

        open_position_page.third_job_title()
        assert open_position_page.third_job_title() == 'Software Quality Assurance Engineer (Remote)'

        open_position_page.check_location()
        assert open_position_page.check_location() == '×All'

        open_position_page.check_department()
        assert open_position_page.check_department() == '×Quality Assurance'




