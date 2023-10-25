import pytest
from Page_Object_Model.src.Pages.Home_Page import HomePage
from Page_Object_Model.src.Pages.General_Career_Page import GeneralCareerPage


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid15
    def test_insider_home_page_is_opened(self):
        home_page = HomePage(self.driver)
        general_career_page = GeneralCareerPage(self.driver)
        home_page.go_to_home_page()
        home_page.accept_cookies()
        home_page.click_company_in_navigation_bar()
        home_page.select_career_option()
        general_career_page.go_to_general_career_page()
        general_career_page.get_page_title_text()
        assert general_career_page.get_page_title_text() == 'Ready to disrupt?'


