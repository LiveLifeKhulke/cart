import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name",action='store',default='firefox')

@pytest.fixture(scope = 'class')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path='c:\\geckodriver.exe')
    driver.maximize_window()
    request.cls.driver = driver