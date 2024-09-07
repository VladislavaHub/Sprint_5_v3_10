from xz.config import Configuration
from xz.locators import LocatorsBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from xz.data import UserData
from xz.helpers import get_sign_up_data


class TestRegistration:

    def test_signup(self, driver):
        driver.find_element(*LocatorsBurgers.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsBurgers.REGISTER_BUTTON))
        driver.find_element(*LocatorsBurgers.REGISTER_BUTTON).click()
        email, password = get_sign_up_data()

        driver.find_element(*LocatorsBurgers.NAME_FIELD).send_keys(UserData.LOGIN)
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(email)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LocatorsBurgers.REGISTER_FINAL_BUTTON).click()
        WebDriverWait(driver, 7).until(EC.url_to_be(Configuration.URL_INPUT))

        assert driver.current_url == Configuration.URL_INPUT

    def test_empty_name(self, driver):
        driver.get(Configuration.URL_REG)
        WebDriverWait(driver, 6).until(EC.url_to_be(Configuration.URL_REG))
        email, password = get_sign_up_data()

        name_field = driver.find_element(*LocatorsBurgers.NAME_FIELD)
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(email)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LocatorsBurgers.REGISTER_FINAL_BUTTON).click()


        assert name_field.get_attribute("value") == ""
        assert driver.current_url != Configuration.URL_INPUT

    def test_incorrect_password(self, driver):
        driver.get(Configuration.URL_REG)
        WebDriverWait(driver, 4).until(EC.url_to_be(Configuration.URL_REG))
        email = get_sign_up_data()

        driver.find_element(*LocatorsBurgers.NAME_FIELD).send_keys(UserData.LOGIN)
        driver.find_element(*LocatorsBurgers.EMAIL_FIELD).send_keys(email)
        driver.find_element(*LocatorsBurgers.PASSWORD_FIELD).send_keys("sssss")
        driver.find_element(*LocatorsBurgers.REGISTER_FINAL_BUTTON).click()

        message_incorrect_password = (WebDriverWait(driver, 4).
        until(expected_conditions.visibility_of_element_located(LocatorsBurgers.MESSAGE_INCORRECT_PASSWORD)))

        assert driver.current_url != Configuration.URL_INPUT
        assert message_incorrect_password.is_enabled()
        assert message_incorrect_password.is_displayed()