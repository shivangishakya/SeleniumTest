import unittest, warnings, time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProfilePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        email = self.driver.find_element(by=By.NAME, value='email')
        email.send_keys("test1@test.com")
        time.sleep(2)
        email.submit()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[3]').click()
        time.sleep(2)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_current_url(self):
        current_url = self.driver.current_url
        self.assertIn(current_url, "http://localhost:3000/profile")

    def test_get_page_heading(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div/h2')
        time.sleep(2)
        self.assertIn(elem.text, "My Trips")

    def test_get_page_email_id(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div/h5')
        time.sleep(2)
        self.assertIn(elem.text, "TEST1@TEST.COM")

    def test_get_empty_trips(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/p')
        time.sleep(2)
        self.assertIn(elem.text, "You haven't booked any trips")

    def test_redirect_to_home(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[1]')
        time.sleep(2)
        elem.click()
        time.sleep(2)
        self.assertIn(self.driver.current_url, "http://localhost:3000/")

    def test_get_some_trip(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[1]')
        time.sleep(2)
        elem.click()
        time.sleep(2)
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/a[1]')
        time.sleep(2)
        elem.click()
        time.sleep(2)
        self.assertIn(self.driver.current_url, "http://localhost:3000/launch/109")

        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div[3]/button')
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        self.assertIn(elem.text, "ADD TO CART")

        elem.click()
        time.sleep(5)
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div[3]/button')
        self.assertIn(elem.text, "REMOVE FROM CART")

        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[2]')
        self.assertIn(button.text, "CART")
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        button.click()
        time.sleep(5)
        self.assertIn(self.driver.current_url, "http://localhost:3000/cart")

        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/a')
        self.assertIn(elem.text, "Starlink-15 (v1.0)\nFALCON 9")
        time.sleep(5)
        elem.click()
        time.sleep(5)
        self.assertIn(self.driver.current_url, "http://localhost:3000/launch/109")

        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[2]')
        self.assertIn(button.text, "CART")
        time.sleep(5)
        button.click()
        time.sleep(5)
        self.assertIn(self.driver.current_url, "http://localhost:3000/cart")

        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/button')
        self.assertIn(button.text, "BOOK ALL")
        time.sleep(5)
        button.click()
        time.sleep(2)

        self.driver.get("http://localhost:3000/profile")

        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/a')
        time.sleep(5)
        self.assertIn(elem.text, "Starlink-15 (v1.0)\nFALCON 9") 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)
    