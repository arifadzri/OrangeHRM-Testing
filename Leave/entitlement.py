import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Entitlement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        #==================================================#
        #                  ADD ENTITLEMENT                 #
        #==================================================#

    def test_1_add_entitlement(self):
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
        #Dashboard - Leave - Entitlement
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_leave_viewLeaveModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_leave_Entitlements")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_leave_addLeaveEntitlement").click()
        time.sleep(2)
        #Add Entitlement
         #Empliyee Name
        driver.find_element(By.ID, "entitlements_employee_empName").click()
        pyautogui.typewrite("Anthony Nolan")
        pyautogui.press("enter")
        time.sleep(5)
         #Leave Type
        leavetype = Select(driver.find_element(By.ID, "entitlements_leave_type")) 
        leavetype.select_by_visible_text("US - FMLA")
        time.sleep(2)
         #Leave Period
        leavepriod = Select(driver.find_element(By.ID, "period")) 
        leavepriod.select_by_visible_text("2021-01-01 - 2021-12-31")
        time.sleep(2)
         #Entitlement
        driver.find_element(By.ID, "entitlements_entitlement").send_keys(10000)
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.CSS_SELECTOR, "input#btnSave").click()
        time.sleep(2)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("Added", response_data)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()