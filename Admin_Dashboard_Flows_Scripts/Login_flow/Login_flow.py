import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://admin-spruce-qa.appnofy.com/auth/sign-in")
        print("Browser initialized and navigated to login page.")

    def find_element_with_wait(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.fail(f"Element {locator} not found within timeout.")

    def test_successful_login(self):
        email_input = self.find_element_with_wait((By.ID, "email"))
        password_input = self.find_element_with_wait((By.ID, "password"))
        submit_button = self.find_element_with_wait((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/form/button'))

        email_input.send_keys("andrew@getspruce.com")
        password_input.send_keys("click123")
        submit_button.click()

        dashboard_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]'))
        )
        self.assertTrue(dashboard_element.is_displayed(), "Dashboard element not displayed.")
        print("Successful login test passed.")

    def test_failed_login(self):
        email_input = self.find_element_with_wait((By.ID, "email"))
        password_input = self.find_element_with_wait((By.ID, "password"))
        submit_button = self.find_element_with_wait((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/form/button'))

        email_input.send_keys("test@test.com")
        password_input.send_keys("abcd$1234")
        submit_button.click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message"))
        )
        self.assertTrue(error_message_element.is_displayed(), "Error message not displayed for failed login.")
        print("Failed login test passed.")

    def test_empty_email_field(self):
        password_input = self.find_element_with_wait((By.ID, "password"))
        submit_button = self.find_element_with_wait((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/form/button'))

        password_input.send_keys("click123")
        submit_button.click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message"))
        )
        self.assertTrue(error_message_element.is_displayed(), "Error message not displayed for empty email.")
        print("Empty email field test passed.")

    def test_empty_password_field(self):
        email_input = self.find_element_with_wait((By.ID, "email"))
        submit_button = self.find_element_with_wait((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/form/button'))

        email_input.send_keys("andrew@getspruce.com")
        submit_button.click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message"))
        )
        self.assertTrue(error_message_element.is_displayed(), "Error message not displayed for empty password.")
        print("Empty password field test passed.")

    def test_invalid_email_format(self):
        email_input = self.find_element_with_wait((By.ID, "email"))
        password_input = self.find_element_with_wait((By.ID, "password"))
        submit_button = self.find_element_with_wait((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/form/button'))

        email_input.send_keys("invalid-email")
        password_input.send_keys("click123")
        submit_button.click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message"))
        )
        self.assertTrue(error_message_element.is_displayed(), "Error message not displayed for invalid email format.")
        print("Invalid email format test passed.")

    def tearDown(self):
        self.driver.quit()
        print("Browser session ended.")


if __name__ == "__main__":
    unittest.main()
