import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class ProjectInfo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        #==================================================#
        #                   ADD CUSTOMER                   #
        #==================================================#

    def test_1_add_customer(self):
        #Open Website
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/") 
        driver.implicitly_wait(2)
        driver.maximize_window()
        time.sleep(2)
        #Login
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") 
        time.sleep(2)
        driver.find_element(By.ID,"btnLogin").click() 
        time.sleep(2)
        #Dashboard - Time - Project Info
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_time_viewTimeModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_ProjectInfo")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewCustomers").click()
        time.sleep(2)
        #Add Customer
         #Click Add Button
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID, "addCustomer_customerName").send_keys("1Admin")
        time.sleep(2)
        driver.find_element(By.ID, "addCustomer_description").send_keys("Admin is a")
        time.sleep(2)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("1Admin", response_data)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()