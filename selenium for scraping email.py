from selenium import webdriver
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()
driver.get("https://unbxd.com/contact-us/")

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find email addresses
emails = set()
for tag in soup.find_all(re.compile("^[\w.+-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$")):
    emails.add(tag.text)

# Print found email addresses
for email in emails:
    print("Email address found:", email)

# Close the webdriver
driver.quit()


