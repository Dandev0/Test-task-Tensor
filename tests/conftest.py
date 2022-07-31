import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = chrome_options()
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options,
                              executable_path='C:\\Users\Danil\PycharmProjects\page_object\chromedriver_win32/chromedriver.exe')
    yield driver
    driver.quit()
