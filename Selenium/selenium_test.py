from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
wait =  WebDriverWait(driver, timeout=10)

driver.get("https://parabank.parasoft.com/")
wait.until(lambda d: driver.find_element(By.NAME,"username").is_displayed())
driver.find_element(By.NAME,"username").send_keys("aaa")
driver.find_element(By.NAME,"password").send_keys("aaa")
driver.find_element(By.XPATH,'//*[@value="Log In"]').click()
wait.until(lambda d: driver.find_element(By.XPATH,'//*[text()="Welcome"]').is_displayed())