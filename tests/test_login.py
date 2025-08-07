from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")

# Wait for username field and enter credentials
wait = WebDriverWait(driver, 10)
username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Verify successful login by checking page title or URL
# wait.until(EC.url_contains())
WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
driver.save_screenshot("screenshots/login.png")
print("Login successful. Current URL:", driver.current_url)

driver.quit()