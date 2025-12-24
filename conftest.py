from email.policy import default
import allure
import pytest
from selenium import webdriver
from pathlib import Path
from datetime import datetime

from pages.login_page import LoginPage

SCREENSHOT_DIR = Path("screenshots")

url = "https://www.saucedemo.com"
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="safari",
        help="please choose browser type"
    )


@pytest.fixture(scope="function")
def setup_driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

login_data = [{"username":"standard_user","password":"secret_sauce"}]
@pytest.fixture(params=login_data)
def get_login_data(request):
    return request.param
@pytest.fixture
def logged_in_driver(setup_driver,get_login_data):
    driver = setup_driver
    login_page = LoginPage(driver)
    login_success = login_page.do_login(url, get_login_data["username"], get_login_data["password"])
    #assert login_success, "Login failed — stopping test execution"
    return driver, login_success


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup_driver")
        if driver:
            SCREENSHOT_DIR.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = SCREENSHOT_DIR / file_name

            # Save screenshot to directory
            driver.save_screenshot(str(file_path))

            # Attach to Allure
            allure.attach.file(
                str(file_path),
                name=file_name,
                attachment_type=allure.attachment_type.PNG
            )