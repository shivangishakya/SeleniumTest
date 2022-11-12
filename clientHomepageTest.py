import unittest, warnings, time
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_title(self):
        self.assertIn("Launches", self.driver.title)

    def test_login(self):
        email = self.driver.find_element(by=By.NAME, value='email')
        time.sleep(2)
        email.send_keys("test1@test.com")
        time.sleep(2)
        email.submit()
        self.assertIn(self.driver.current_url, "http://localhost:3000/")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)