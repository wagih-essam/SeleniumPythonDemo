from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProject_2.Pages.Loginpage import LoginPage
from SampleProject_2.Pages.Homepage import HomePage
import HtmlTestRunner

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/c.city/PycharmProjects/PyDemo/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_Login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/c.city/PycharmProjects/PyDemo/SampleProject_2/Reports'),verbosity=2)

