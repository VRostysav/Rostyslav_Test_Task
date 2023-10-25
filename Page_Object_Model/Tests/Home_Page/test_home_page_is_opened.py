import pytest
from Page_Object_Model.src.Pages.Home_Page import HomePage


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_insider_home_page_is_opened(self):
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.get_home_page_title()
        assert home_page.get_home_page_title() == "The#1 platform for individualized,cross-channel customer experiences"
