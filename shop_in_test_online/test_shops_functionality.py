from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestShopsFunctionality(unittest.TestCase):

    def test_finding_iphone_phones(self):
        # Given
        da_url = "https://ecommerce-playground.lambdatest.io/"
        da_searchbar_textfield = "//input[@name='search']"
        da_searchbar_button = "//button[@type='submit']"
        da_first_iphone = "//*/a[text()='iPhone']"

        test_phrase = "iphone"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(da_url)

        # When
        da_gui_searchbar = driver.find_element(By.XPATH, da_searchbar_textfield)
        da_gui_searchbar.click()
        da_gui_searchbar.send_keys(test_phrase)
        driver.find_element(By.XPATH, da_searchbar_button).click()

        # Then
        actual_presence = driver.find_element(By.XPATH, da_first_iphone).is_displayed()
        self.assertTrue(actual_presence)


if __name__ == '__main__':
    unittest.main()
