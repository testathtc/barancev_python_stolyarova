from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class My123(unittest.TestCase):
    def setUp(self):
        #mock comment
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://xubuntu/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_123(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        #driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        #driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        self.assertTrue(self.is_element_present(By.XPATH, "//*[@id='wrapper']/header//nav//li[2]"))
        self.assertEqual("My profile", driver.find_element_by_xpath("//*[@id='wrapper']/header//nav//li[2]").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
