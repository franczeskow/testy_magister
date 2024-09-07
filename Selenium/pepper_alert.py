from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time
# Initialize the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("-disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=options)  # or use any other driver
driver.get("https://www.pepper.pl/")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()=" Akceptuj wszystkie "]'))).click()
driver.find_element(By.XPATH, "//button[@class='button--toW5-square space--ml-2 button button--shape-circle button--type-primary button--mode-white']").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='jan@kowalski.pl']")))
email_input = driver.find_element(By.XPATH, "//input[@placeholder='jan@kowalski.pl']")
email_input.send_keys("tescicki123")
driver.find_element(By.XPATH, "//span[contains(text(), 'Kontynuuj')]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='**************']")))
password_input = driver.find_element(By.XPATH, "//input[@placeholder='**************']")
password_input.send_keys("tajnehaslo123")
driver.find_element(By.XPATH, "//span[text()=' Zaloguj Się ']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//img[@alt="Awatar użytkownika tescicki123"]')))

# Navigate to alerts
driver.find_element(By.XPATH, '//img[@alt="Awatar użytkownika tescicki123"]').click()
driver.find_element(By.XPATH, '//a[text()=" Lista alertów "]').click()
driver.find_element(By.XPATH, '//span[text()="Zarządzaj alertami"]').click()
alert_input = driver.find_element(By.XPATH, "//input[@placeholder='Twój alert...']")
alert_input.click()
alert_input.send_keys("telefony")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//ol/li/div/span[text()=" Telefony "]')))
driver.find_element(By.XPATH, '//ol/li/div/span[text()=" Telefony "]').click()
driver.find_element(By.XPATH, "//span[contains(text(), 'Utwórz nowy alert')]").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'telefony')]")))

driver.quit()