from selenium.webdriver.common.by import By


class CareerPageLocators:
    LOCATIONS_LIST = (By.CSS_SELECTOR, 'ul.glide__slides div.location-info p.mb-0')
    COOKIES = (By.CSS_SELECTOR, '#wt-cli-accept-all-btn')
    PAGE_TITLE = (By.CSS_SELECTOR, 'h1.big-title-media')

