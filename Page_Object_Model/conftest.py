import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    parent_handle = driver.current_window_handle
    request.cls.driver = driver
    request.cls.parent_handle = parent_handle
    yield
    driver.quit()
