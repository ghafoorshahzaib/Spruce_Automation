import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RememberMeTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://admin-spruce.appnofy.com/auth/sign-in")

    def test_remember_me(self):
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        remember_me_checkbox = self.driver.find_element(By.ID, "remember_me_checkbox")
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')

        email_input.send_keys("koderlabs.admin@mailinator.com")
        password_input.send_keys("click123")
        remember_me_checkbox.click()
        submit_button.click()

        dashboard_element = self.driver.find_element(By.ID, "dashboard")
        self.assertTrue(dashboard_element.is_displayed())
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]')))
        dashboard_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/aside/div/div[2]/ul/li[1]/span[2]')
        self.assertTrue(dashboard_element.is_displayed())

        self.driver.quit()

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.get("https://admin-spruce.appnofy.com/auth/sign-in")

        dashboard_element = self.driver.find_element(By.ID, "dashboard")
        self.assertTrue(dashboard_element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
