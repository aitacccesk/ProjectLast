from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.reddit.com/")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys("aytac1110")
password_input.send_keys("Bf@c4m6arWuPtU6")

login_button2 = driver.find_element(By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
login_button2.click()

time.sleep(10)

profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()

time.sleep(2)

dark_mode_button = driver.find_element(By.XPATH, '//*[@id="darkmode-list-item"]/div/span[1]/span[2]/span[1]')
dark_mode_button.click()

time.sleep(5)
driver.quit()
