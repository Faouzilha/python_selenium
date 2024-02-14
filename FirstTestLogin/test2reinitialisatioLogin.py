# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test2ReinitialisationLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_2_reinitialisation_login(self):
        driver = self.driver
        driver.get("https://phptravels.net/login")
        driver.find_element(By.XPATH,"//form[@id='login']/div/div/div/div[3]/div").click()
        driver.find_element(By.ID,"rememberchb").click()
        driver.find_element(By.XPATH,"//form[@id='login']/div/div/div/div[3]/div[2]/label/font/font").click()
        driver.find_element(By.ID,"reset_mail").click()
        driver.find_element(By.ID,"reset").click()
        driver.find_element(By.ID,"reset_mail").clear()
        driver.find_element(By.ID,"reset_mail").send_keys("lola@php.net")
        driver.find_element(By.XPATH,"//form[@id='forget_pass']/div[2]/button[2]").click()
        self.assertEqual("Invalid or no account found with this email", self.close_alert_and_get_its_text())
        driver.find_element(By.ID,"login").click()
        driver.find_element(By.XPATH,"//form[@id='login']/div/div/div/div[4]/div[3]/div/a/span/font/font").click()
        driver.get("https://phptravels.net/signup")
        driver.find_element(By.ID,"user_email").clear()
        driver.find_element(By.ID,"user_email").send_keys("lola@php.net")
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("lilou")
        driver.find_elemen(By.ID,"firstname").click()
        driver.find_element(By.ID,"firstname").clear()
        driver.find_element(By.ID,"firstname").send_keys("LILOU")
        driver.find_element(By.ID,"last_name").click()
        driver.find_element(By.ID,"last_name").clear()
        driver.find_element(By.ID,"last_name").send_keys("Lola")
        driver.find_element(By.XPATH,"//form[@id='signup']/div/div/div/div[3]/div/div/div/button/div/div/div").click()
        driver.find_element(By.XPATH,"//input[@type='search']").clear()
        driver.find_element(By.XPATH,"//input[@type='search']").send_keys("fran")
        driver.find_element(By.XPATH,"//a[@id='bs-select-1-73']/span").click()
        Select(driver.find_element_by_name("phone_country_code")).select_by_visible_text("")
        driver.find_element(By.ID,"phone").click()
        driver.find_element(By.ID,"phone").clear()
        driver.find_element(By.ID,"phone").send_keys("0501843215")
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element(By.XPATH,"//span[@id='recaptcha-anchor']/div").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element(By.XPATH,"//button[@id='submitBTN']/font/font").click()
        driver.find_element(By.XPATH,"//body[@id='fadein']/div[3]").click()
    


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
