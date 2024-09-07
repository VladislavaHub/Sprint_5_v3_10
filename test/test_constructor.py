from xz.config import Configuration
from xz.locators import LocatorsBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xz.data import UserData


class TestConstructor:

    def test_section_bulki(self, driver):
        sous_section = driver.find_element(*LocatorsBurgers.SOUS_SECTION)
        sous_section.click()
        nachinki_section = driver.find_element(*LocatorsBurgers.NACHINKI_SECTION)
        nachinki_section.click()
        bulki_section = driver.find_element(*LocatorsBurgers.BULKI_SECTION)
        bulki_section.click()
        WebDriverWait(driver, 4).until(EC.url_to_be(Configuration.URL))
        assert "current" in bulki_section.get_attribute("Class")
        assert "current" not in nachinki_section.get_attribute("Class")
        assert "current" not in bulki_section.get_attribute("Class")


    def test_section_sous(self, driver):
        sous_section = driver.find_element(*LocatorsBurgers.SOUS_SECTION)
        nachinki_section = driver.find_element(*LocatorsBurgers.NACHINKI_SECTION)
        bulki_section = driver.find_element(*LocatorsBurgers.BULKI_SECTION)
        sous_section.click()
        WebDriverWait(driver, 4).until(EC.url_to_be(Configuration.URL))
        assert "current" in sous_section.get_attribute("Class")
        assert "current" not in sous_section.get_attribute("Class")
        assert "current" not in bulki_section.get_attribute("Class")


    def test_section_nachinki(self, driver):
        sous_section = driver.find_element(*LocatorsBurgers.SOUS_SECTION)
        bulki_section = driver.find_element(*LocatorsBurgers.BULKI_SECTION)
        nachinki_section = driver.find_element(*LocatorsBurgers.NACHINKI_SECTION)
        nachinki_section.click()
        WebDriverWait(driver, 4).until(EC.url_to_be(Configuration.URL))
        assert "current" in nachinki_section.get_attribute("Class")
        assert "current" not in sous_section.get_attribute("Class")
        assert "current" not in nachinki_section.get_attribute("Class")

