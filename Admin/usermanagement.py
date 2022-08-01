import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class UserManagement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        #==================================================#
        #                    ADD USER                      #
        #==================================================#

    def test_a_add_user_on_user_management(self):
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
        #Dashboard - Admin - User Management - User
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_UserManagement")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewSystemUsers").click()
        time.sleep(2)
        #Add Users
         #Click Add Button
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
         #User Role
        userrole = Select(driver.find_element(By.ID, "systemUser_userType")) 
        userrole.select_by_visible_text("Admin")
        time.sleep(2)
         #Employee Name
        driver.find_element(By.ID, "systemUser_employeeName_empName").click()
        pyautogui.typewrite("Admin A")
        pyautogui.press("enter")
        time.sleep(5)
         #User Name
        driver.find_element(By.ID,"systemUser_userName").send_keys("111AAA")
        time.sleep(2)
         #Status
        status = Select(driver.find_element(By.ID, "systemUser_status"))
        status.select_by_visible_text("Enabled")
        time.sleep(2)
         #Password
        driver.find_element(By.ID,"systemUser_password").send_keys("admin123") 
        time.sleep(2)
         #Confirm Password
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("admin123") 
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(10)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("111AAA", response_data)

        #==================================================#
        #                 SEARCH USER                      #
        #==================================================#

    def test_a_search_user(self):
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
        #Dashboard - Admin - User Management - User
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_UserManagement")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewSystemUsers").click()
        time.sleep(2)
        #Search Data
         #Input Username
        driver.find_element(By.ID, "searchSystemUser_userName").send_keys("Admin")
        time.sleep(2)
         #Select User Role
        userrole = Select(driver.find_element(By.ID, "searchSystemUser_userType")) 
        userrole.select_by_visible_text("Admin")
        time.sleep(2)
         #Click Search
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)   
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("Admin", response_data)

        #==================================================#
        #               SEARCH USER NEGATIF                #
        #==================================================#

    def test_a_search_user_negatif(self):
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
        #Dashboard - Admin - User Management - User
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_UserManagement")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewSystemUsers").click()
        time.sleep(2)
        #Search Data
         #Input Username
        driver.find_element(By.ID, "searchSystemUser_userName").send_keys("xxxxxxxx")
        time.sleep(2)
         #Click Search
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("No Records Found", response_data)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()