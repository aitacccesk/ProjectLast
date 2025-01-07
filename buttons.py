from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Wait and click the Chat button
chat_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="header-action-item-chat-button"]'))
)
chat_button.click()

time.sleep(3)

# Wait and click the Create Post button
create_post_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="create-post"]'))
)
create_post_button.click()

time.sleep(3)

# Wait and click the Inbox button
inbox_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mini-inbox-tooltip"]/span/faceplate-tracker/faceplate-tooltip/button'))
)
inbox_button.click()

time.sleep(5)

driver.quit()
