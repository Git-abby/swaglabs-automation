
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
# Driver function
def driver():
    options = Options()
    # options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add first product to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Add to inventory by product Name Sauce Labs Bolt T-Shirt - add-to-cart-sauce-labs-bolt-t-shirt
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    # Verify cart count
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_count.text == "2"
    print("🛍️ Product added to cart successfully.")

