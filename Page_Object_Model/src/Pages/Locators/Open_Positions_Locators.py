from selenium.webdriver.common.by import By


class OpenPositionsLocators:
    LOCATION_DROPDOWN = (By.CSS_SELECTOR, '#select2-filter-by-location-container')
    All_OPTION = (By.CSS_SELECTOR, 'li.select2-results__option:nth-of-type(1)')
    FIRST_JOB_TITLE = (By.CSS_SELECTOR, 'div.full-timeremote:nth-of-type(1) p.font-weight-bold')
    SECOND_JOB_TITLE = (By.CSS_SELECTOR, 'div.full-timeremote:nth-of-type(2) p.font-weight-bold')
    THIRD_JOB_TITLE = (By.CSS_SELECTOR, 'div.full-timeremote:nth-of-type(4) p.font-weight-bold')

    DEPARTMENT_NAME = (By.CSS_SELECTOR, '#select2-filter-by-department-container')
    LOCATION = (By.CSS_SELECTOR, '#select2-filter-by-location-container')

    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, 'div.position-list-item:nth-of-type(1) a.btn-navy')
    COOKIES = (By.CSS_SELECTOR, '#wt-cli-accept-all-btn')

    BROWSE_OPEN_POSITIONS = (By.CSS_SELECTOR, 'h3.mb-0')
