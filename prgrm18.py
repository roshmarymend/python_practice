from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(By.ID, "userName").send_keys("John")
driver.find_element(By.ID, "userEmail").send_keys("john@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Kerala")
driver.find_element(By.ID, "permanentAddress").send_keys("India")

submit = driver.find_element(By.ID, "submit")

# Scroll the button into view
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});", submit
)

# Try normal click
try:
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
except Exception:
    # If an advertisement blocks the button
    driver.execute_script("arguments[0].click();", submit)

# Display the result
result = wait.until(
    EC.visibility_of_element_located((By.ID, "output"))
)
print(result.text)
driver.quit()