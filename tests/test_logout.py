from pages.logout_page import LogoutPage
import allure


@allure.title("Test: Logout test")
@allure.description("Verify that user is able to logout successfully")
def test_logout(logged_in_driver):
    driver, login_success = logged_in_driver
    assert login_success, "Login failed, Stoping the test execution"
    logout_page = LogoutPage(driver)
    assert logout_page.do_logout(), "Logout failed"
