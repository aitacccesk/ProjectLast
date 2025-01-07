from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.reddit.com/")

# Login process
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_button.click()

username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_input.send_keys("aytac1110")

password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys("Bf@c4m6arWuPtU6")

login_button2 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button'))
)
login_button2.click()

time.sleep(10)

# Open Profile Menu
profile_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="expand-user-drawer-button"]'))
)
profile_menu.click()

time.sleep(2)

# Click on Avatar to open options
avatar_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="user-drawer-content"]/ul[1]/faceplate-tracker[2]/li/a'))
)
avatar_button.click()

time.sleep(2)

# Click on the "Edit Avatar" button
edit_avatar_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/shreddit-app/div[1]/div/nav/faceplate-tracker[2]/a'))
)
edit_avatar_button.click()

time.sleep(3)

# Quit the browser after the actions
driver.quit()
