from xz.config import Configuration
from xz.locators import LocatorsBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xz.data import UserData


class TestLoginInToYourPersonalAccount:

    def test_log_in_to_your_personal_account(self, driver):
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*LocatorsBurgers.INPUT_MAIN_BUTTON).click()
        driver.find_element(*LocatorsBurgers.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Configuration.URL_ACCOUNT_PROFILE))
        sections = driver.find_element(*LocatorsBurgersм.SECTIONS)
        assert driver.current_url == Configuration.URL_ACCOUNT_PROFILE
        driver.quit()