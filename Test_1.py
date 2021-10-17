import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
adminField=driver.find_element_by_name("txtUsername")
adminField.send_keys("Admin")
passField=driver.find_element_by_name("txtPassword")
passField.send_keys("admin123")
button=driver.find_element_by_name("Submit")
button.click()
pimPage=driver.find_element_by_id("menu_pim_viewPimModule")
pimPage.click()
time.sleep(3)
pimPageAddEmp=driver.find_element_by_id("menu_pim_addEmployee")
pimPageAddEmp.click()
empName=driver.find_element_by_id("firstName")
empName.send_keys("EmpName")
empLastName=driver.find_element_by_id("lastName")
empLastName.send_keys("EmpLastName")
saveButton=driver.find_element_by_id("btnSave")
saveButton.click()
driver.quit()