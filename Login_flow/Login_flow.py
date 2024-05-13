import tracemalloc
tracemalloc.start()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://admin-spruce.appnofy.com/auth/sign-in")

    def test_successful_login(self):
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')

        email_input.send_keys("koderlabs.admin@mailinator.com")
        password_input.send_keys("click123")
        submit_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]')))
        dashboard_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]')
        self.assertTrue(dashboard_element.is_displayed())

    def test_failed_login(self):
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')

        email_input.send_keys("test@test.com")
        password_input.send_keys("abcd$1234")
        submit_button.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message")))
        error_message_element = self.driver.find_element(By.CLASS_NAME, "ant-notification-notice-message")
        self.assertTrue(error_message_element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
# class="ant-notification-notice-message"