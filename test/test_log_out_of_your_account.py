from xz.config import Configuration
from xz.locators import LocatorsBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xz.data import UserData


class TestLogOutOfYourAccount:

    def test_log_out_of_your_account(self, driver):
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        driver.find_element(*LocatorsBurgers.ACCOUNT_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Configuration.URL_INPUT))
        assert driver.current_url == Configuration.URL_INPUT