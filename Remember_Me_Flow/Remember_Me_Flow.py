import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RememberMeTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver (in this example, Chrome WebDriver)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # Navigate to the login page
        self.driver.get("https://admin-spruce.appnofy.com/auth/sign-in")

    def test_remember_me(self):
        # Locate the email and password fields
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        remember_me_checkbox = self.driver.find_element(By.ID, "remember_me_checkbox")
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')

        # Enter valid credentials
        email_input.send_keys("koderlabs.admin@mailinator.com")
        password_input.send_keys("click123")
        # Check the "Remember Me" checkbox
        remember_me_checkbox.click()

        # Click the login button
        submit_button.click()

        # Verify that the login was successful by checking for presence of a dashboard element
        dashboard_element = self.driver.find_element(By.ID, "dashboard")
        self.assertTrue(dashboard_element.is_displayed())
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]')))
        dashboard_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]')
        self.assertTrue(dashboard_element.is_displayed())


        # Close the browser session
        self.driver.quit()

        # Open a new browser session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Navigate to the website (this could also be the base URL if login redirects to another page)
        self.driver.get("https://admin-spruce.appnofy.com/auth/sign-in")

        # Verify that the user is already logged in due to "Remember Me" functionality
        dashboard_element = self.driver.find_element(By.ID, "dashboard")
        self.assertTrue(dashboard_element.is_displayed())

    def tearDown(self):
        # Clean up after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
