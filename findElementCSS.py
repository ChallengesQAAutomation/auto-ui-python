from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome
chrome_options = ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-extensions')
chrome_driver_path = 'chromedriver'
chrome_service = ChromeService(executable_path=chrome_driver_path)

chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

chrome_driver.get("https://jsonplaceholder.typicode.com/guide/")
css_selector='body > div:nth-child(2) > main > h3:nth-child(5)'
wait = WebDriverWait(chrome_driver, 20)
h3_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

h3_element = chrome_driver.find_element(By.CSS_SELECTOR, css_selector)
h3_text = h3_element.text
print("Texto de h3:", h3_text)

chrome_driver.quit()
