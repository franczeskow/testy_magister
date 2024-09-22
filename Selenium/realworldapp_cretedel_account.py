from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time()
# Initialize the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("-disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=options) 


driver.get("http://localhost:3000/")
driver.find_element(By.ID, "username").send_keys("Heath93")
driver.find_element(By.ID, "password").send_keys("s3cret")
driver.find_element(By.CSS_SELECTOR, "[data-test='signin-submit']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='sidenav-user-full-name']")))

driver.find_element(By.CSS_SELECTOR, '[data-test="sidenav-bankaccounts"]').click()

# Click on the new bank account button
driver.find_element(By.CSS_SELECTOR, '[data-test="bankaccount-new"]').click()

# Fill in the bank account details
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Bank Name"]').send_keys("nowe konto")
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Routing Number"]').send_keys("999999999")
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Account Number"]').send_keys("000000000")

# Submit the bank account form
driver.find_element(By.CSS_SELECTOR, '[data-test="bankaccount-submit"]').click()

# Wait for the last bank account item to be visible and check its text
last_table_account_item = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test*="bankaccount-list-item"]:last-child'))
)

assert "nowe konto" in last_table_account_item.text

# Click the delete button for the last bank account item
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test*="bankaccount-list-item"]:last-child > div > div > button')))
driver.find_element(By.CSS_SELECTOR, '[data-test*="bankaccount-list-item"]:last-child > div > div > button').click()


last_table_account_item = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test*="bankaccount-list-item"]:last-child'))
)
# Verify the account is marked as deleted
assert "nowe konto (Deleted)" in last_table_account_item.text

# Close the driver
driver.quit()
print("--- %s seconds ---" % (time.time() - start_time))