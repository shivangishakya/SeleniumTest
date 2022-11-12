import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import time

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:4000/")
        time.sleep(5)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_title(self):
        self.assertIn(self.driver.title, "Apollo Server")
 
    def test_homepage_text(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]')
        expected_text = 'Welcome to Apollo Server\nIt appears that you might be offline. POST to this endpoint to query your graph:\ncurl --request POST \\\n  --header \'content-type: application/json\' \\\n  --url \'http://localhost:4000/\' \\\n  --data \'{"query":"query { __typename }"}\''
        self.assertIn(elem.text, expected_text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)
    