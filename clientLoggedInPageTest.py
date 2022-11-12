import unittest, warnings, time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoggedInPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        email = self.driver.find_element(by=By.NAME, value='email')
        email.send_keys("test1@test.com")
        time.sleep(2)
        email.submit()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_Heading2(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div/h2')
        time.sleep(2)
        self.assertIn(elem.text, "Space Explorer")

    def test_loggedin_email_id(self):
        elem = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div/h5')
        time.sleep(2)
        self.assertIn(elem.text, "TEST1@TEST.COM")

    def test_element_a1_text(self):
        elem1 = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/a[1]/h3')
        elem2 = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/a[1]/h5')
        time.sleep(2)
        self.assertIn(elem1.text, "Starlink-15 (v1.0)")
        self.assertIn(elem2.text, "FALCON 9")

    def test_count_visible_elements(self):
        elem = self.driver.find_elements(by=By.XPATH, value='//*[@id="root"]/div[2]/a')
        time.sleep(2)
        self.assertEqual(len(elem), 20)

    def test_get_loadmore_button(self):
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[@class="css-1on771l"]/button')
        time.sleep(2)
        self.assertIn(button.text, "LOAD MORE")

    def test_get_home_button(self):
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[1]')
        time.sleep(2)
        self.assertIn(button.text, "HOME")
        button.click()
        time.sleep(2)
        self.assertIn(self.driver.current_url, "http://localhost:3000/")

    def test_get_cart_button(self):
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[2]')
        time.sleep(2)
        self.assertIn(button.text, "CART")
        button.click()
        time.sleep(2)
        self.assertIn(self.driver.current_url, "http://localhost:3000/cart")

    def test_get_profile_button(self):
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/a[3]')
        time.sleep(2)
        self.assertIn(button.text, "PROFILE")
        button.click()
        time.sleep(2)
        self.assertIn(self.driver.current_url, "http://localhost:3000/profile")

    def test_get_logout_button(self):
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/footer/div/button')
        time.sleep(2)
        self.assertIn(button.text, "LOGOUT")
        button.click()
        time.sleep(2)
        self.assertIn(self.driver.current_url, "http://localhost:3000/")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)