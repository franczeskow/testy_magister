from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time()
# Initialize the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("-disable-search-engine-choice-screen")

#Login
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

#comment
driver.find_element(By.XPATH, '(//a[@data-t="threadLink"])[1]').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@placeholder="O czym teraz myślisz..."]')))
driver.find_element(By.XPATH, '//div[@placeholder="O czym teraz myślisz..."]').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"]')))
comment_input = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
comment_input.send_keys("Fajna okazja")
driver.find_element(By.XPATH, '//span[text()="Skomentuj"]').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="comment-body"]/div/div[text()="Fajna okazja"]')))
driver.quit()

print("--- %s seconds ---" % (time.time() - start_time))