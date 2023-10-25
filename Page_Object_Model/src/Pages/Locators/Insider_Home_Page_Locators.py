from selenium.webdriver.common.by import By


class HomePageLocators:
    MAIN_HEADING = (By.CSS_SELECTOR, 'div.d-flex> h1')
    COMPANY_MENU = (By.CSS_SELECTOR, 'li.nav-item:nth-of-type(6) #navbarDropdownMenuLink')
    CAREERS_OPTION = (By.CSS_SELECTOR, 'div.new-menu-dropdown-layout-6-mid-container a.dropdown-sub:nth-of-type(2)')
    COOKIES = (By.CSS_SELECTOR, '#wt-cli-accept-all-btn')




