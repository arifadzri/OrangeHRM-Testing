import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class jobtitles(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        #==================================================#
        #                 ADD JOB TITLE                    #
        #==================================================#
        
    def test_1_add_job_titles(self):
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
        #Dashboard - Admin - Job - Job Titles
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Job")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewJobTitleList").click()
        time.sleep(2)
        #Add Job Title
         #Add Button
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
         #Job Title
        driver.find_element(By.ID, "jobTitle_jobTitle").send_keys("Software Quality Assurance")
        time.sleep(2)
         #Job Description
        driver.find_element(By.ID, "jobTitle_jobDescription").send_keys("Software Quality Assurance same Software Tester")
        time.sleep(2)
         #Note
        driver.find_element(By.ID, "jobTitle_note").send_keys("SQA")
        time.sleep(2)
         #Save Button
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(5)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("Software Quality Assurance", response_data)

        #==================================================#
        #                 ADD PAY GRADES                   #
        #==================================================#

    def test_2_add_pay_grades(self):
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
        #Dashboard - Admin - Job - Pay Grades
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Job")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewPayGrades").click()
        time.sleep(2)
        #Add Pay Grades
         #Add Button
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
         #Pay Grades Name
        driver.find_element(By.ID, "payGrade_name").send_keys("1Grade")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
         #Assigned Currencies
        driver.find_element(By.ID, "btnAddCurrency").click()
        time.sleep(2)
         #Input Currency
        driver.find_element(By.ID, "payGradeCurrency_currencyName").click()
        pyautogui.typewrite("IDR - Indonesian Rupiah")
        pyautogui.press("enter")
        time.sleep(5)
         #Minimum Salary
        driver.find_element(By.ID, "payGradeCurrency_minSalary").send_keys("1000000")
        time.sleep(2)
         #Maximum Salary
        driver.find_element(By.ID, "payGradeCurrency_maxSalary").send_keys("2000000")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.ID, "btnSaveCurrency").click()
        time.sleep(5)
        # validasi
        response_data = driver.find_element(By.ID, "tblCurrencies").text
        self.assertIn("Indonesian Rupiah", response_data)

        #==================================================#
        #             ADD EMPLOYMENT STATUS                #
        #==================================================#

    def test_3_add_employment_status(self):
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
        #Dashboard - Admin - Job - Employment Status
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Job")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_employmentStatus").click()
        time.sleep(2)
        #Add Employment Status
         #Add Button
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
         #Name
        driver.find_element(By.ID, "empStatus_name").send_keys("Work Home Home Full-Time")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(5)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("Work Home Home Full-Time", response_data)

        #==================================================#
        #       ADD EMPLOYMENT STATUS NEGATIF              #
        #==================================================#

    def test_4_add_employment_status_negatif(self):
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
        #Dashboard - Admin - Job - Employment Status
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Job")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_employmentStatus").click()
        time.sleep(2)
        #Add Employment Status
         #Add Button
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
         #Name
        driver.find_element(By.ID, "empStatus_name").send_keys("Work Home Home Full-Time")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(5)
        # validasi
        response_data = driver.find_element(By.ID, "frmEmpStatus").text
        self.assertIn("Already exists", response_data)

        #==================================================#
        #                 ADD JOB CATEGORY                 #
        #==================================================#

    def test_5_add_job_category(self):
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
        #Dashboard - Admin - Job - Job Category
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule")).perform()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Job")).perform()
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_jobCategory").click()
        time.sleep(2)
        #Add Job Category
         #Add Button
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
         #Name
        driver.find_element(By.ID, "jobCategory_name").send_keys("Software Engineer")
        time.sleep(2)
         #Click Save Button
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(5)
        # validasi
        response_data = driver.find_element(By.ID, "resultTable").text
        self.assertIn("Software Engineer", response_data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()