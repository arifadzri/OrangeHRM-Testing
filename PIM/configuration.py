import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Configuration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        #==================================================#
        #               CONFIGURE PIM                      #
        #==================================================#

    def test_1_configure_pim(self):
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
        #Dashboard - PIM - Configuration - Configure PIM
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_pim_viewPimModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_pim_Configuration")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_pim_configurePim").click()
        time.sleep(2)
        #Edit
         #Click Edit Button
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)
         #Click Checkbox on Country Specific Information
        driver.find_element(By.ID, "configPim_chkShowSSN").click()
        time.sleep(2)
        driver.find_element(By.ID, "configPim_chkShowSIN").click()
        time.sleep(2)
        driver.find_element(By.ID, "configPim_chkShowTax").click()
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.CSS_SELECTOR, "input#btnSave").click()
        time.sleep(2)

        #==================================================#
        #               ADD CUSTOM FIELDS                  #
        #==================================================#

    def test_2_add_custom_fields(self):
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
        #Dashboard - PIM - Configuration - Custom Fields
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_pim_viewPimModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_pim_Configuration")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_pim_listCustomFields").click()
        time.sleep(2)
        #Add Custom Fields
         #Clikck Add Button
        driver.find_element(By.ID,"buttonAdd").click()
        time.sleep(2)
         #Input Field Name
        driver.find_element(By.ID, "customField_name").send_keys("Body Type")
        time.sleep(2)
         #Select Screen
        screen = Select(driver.find_element(By.ID, "customField_screen")) 
        screen.select_by_visible_text("Personal Details")
        time.sleep(2)
         #Select Type
        fieldtype = Select(driver.find_element(By.ID, "customField_type")) 
        fieldtype.select_by_visible_text("Text or Number")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.CSS_SELECTOR, "input#btnSave").click()
        time.sleep(2)
        # validasi
        response_data = driver.find_element(By.ID, "customFieldList").text
        self.assertIn("Body Type", response_data)

        #==================================================#
        #                   ADD EMPLOYED                   #
        #==================================================#

    def test_3_add_employed(self):
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
        #Dashboard - PIM 
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_pim_viewPimModule")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_pim_addEmployee").click()
        time.sleep(2)
        #Add Employee
         #Input Full Name
          #First Name
        driver.find_element(By.ID,"firstName").send_keys("Sanbercode")
        time.sleep(2)
          #Last Name
        driver.find_element(By.ID, "lastName").send_keys("Indonesia")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.CSS_SELECTOR, "input#btnSave").click()
        time.sleep(2)
        # validasi
        response_data = driver.find_element(By.ID, "pdMainContainer").text
        self.assertIn("Personal Details", response_data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()