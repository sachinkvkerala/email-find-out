from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
driver.get("https://www.ndtv.com/")

try:
    # Wait for the element with a specific class name to be present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".email-container"))
    )

    # Extract email addresses from the element
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', element.text)

    # Print found email addresses
    for email in emails:
        print("Email address found:", email)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the webdriver
    driver.quit()
