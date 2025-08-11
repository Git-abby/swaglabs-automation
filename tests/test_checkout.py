from test_add_to_cart import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout(driver):
    login(driver)

    # Add products to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))
    assert "cart.html" in driver.current_url
    print("🛒 Navigated to cart")

    # Click checkout
    driver.find_element(By.ID, "checkout").click()
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one.html"))
    print("📦 Checkout started")

    # Fill out user info
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Finalize checkout
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two.html"))
    driver.find_element(By.ID, "finish").click()

    # Verify success
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!"
    driver.save_screenshot("screenshots/checkout.png")
    print("🎉 Checkout completed successfully")