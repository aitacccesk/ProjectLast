from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome setup
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Reddit
driver.get("https://www.reddit.com/")

# Login process
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_button.click()
time.sleep(2)

username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

username_input.send_keys("aytac1110")
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

# Click on Achievements
achievement_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="user-drawer-content"]/ul[1]/faceplate-tracker[3]/li/a'))
)
achievement_button.click()

# Wait for the page to load
time.sleep(5)

# Quit the browser
driver.quit()
