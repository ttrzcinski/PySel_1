from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Test_Shops_Functionality(unittest.TestCase):
    def test_finding_iphone_phones(self):
        da_url = "https://ecommerce-playground.lambdatest.io/"
        da_searchbar_textfield = "//input[@name='search']"
        da_searchbar_button = "//button[@type='submit']"

        test_phrase = "iphone"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(da_url)

        driver.find_element(By.XPATH, da_searchbar_textfield).click()
        driver.find_element(By.XPATH, da_searchbar_textfield).send_keys(test_phrase)
        driver.find_element(By.XPATH, da_searchbar_button).click()

        actual_presence = driver.find_element(By.XPATH, "//*/a[text()='iPhone']").is_displayed()

        self.assertTrue(actual_presence)


if __name__ == '__main__':
    unittest.main()
