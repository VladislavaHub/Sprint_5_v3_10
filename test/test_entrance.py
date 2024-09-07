from xz.config import Configuration
from xz.locators import LocatorsBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xz.data import UserData


class TestEntrance:

    def test_entrance(self, driver):
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Configuration.URL))
        assert driver.current_url == Configuration.URL

    def test_entrance_personal_account(self, driver):
        driver.find_element(*LocatorsBurgers.ACCOUNT_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Configuration.URL))
        assert driver.current_url == Configuration.URL

    def test_entrance_registration_form(self, driver):
        driver.find_element(*LocatorsBurgers.ACCOUNT_BUTTON).click()
        driver.find_element(*LocatorsBurgers.REGISTER_BUTTON).click()
        driver.find_element(*LocatorsBurgers.INPUT_REGISTER_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Configuration.URL))
        assert driver.current_url == Configuration.URL

    def test_entrance_password_recovery(self, driver):
        driver.find_element(*LocatorsBurgers.ACCOUNT_BUTTON).click()
        driver.find_element(*LocatorsBurgers.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*LocatorsBurgers.INPUT_REGISTER_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(ConfConfiguration.URL))
        assert driver.current_url == Configuration.URL