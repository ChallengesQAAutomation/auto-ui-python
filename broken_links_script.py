from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Setup Chrome
chrome_options = ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-extensions')
chrome_driver_path = 'chromedriver'
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Setup Firefox
firefox_options = FirefoxOptions()
firefox_options.add_argument('--start-maximized')
firefox_driver_path = 'geckodriver' 
firefox_service = FirefoxService(executable_path=firefox_driver_path)

# Drivers
chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
firefox_driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

url='https://luiscarlosmarca.github.io/'
# Script Chrome
chrome_driver.get(url)

def find_broken_links_chrome(url):
    chrome_driver.get(url)

    # Wait page
    WebDriverWait(chrome_driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

    links = chrome_driver.find_elements(By.TAG_NAME, 'a')

    broken_links = []

    for link in links:
        href = link.get_attribute('href')
        response = requests.get(href)
        if response.status_code != 200:
            broken_links.append(href)

    return broken_links

broken_links_chrome = find_broken_links_chrome(url)

if len(broken_links_chrome) > 0:
    print('Enlaces rotos encontrados en chrome:')
    for link in broken_links_chrome:
        print(link)
else:
    print('No se encontraron enlaces rotos en chrome.')

chrome_driver.quit()

# Script Firefox
firefox_driver.get(url)

def find_broken_links_firefox(url):
    firefox_driver.get(url)

    # waiting page
    WebDriverWait(firefox_driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

    links = firefox_driver.find_elements(By.TAG_NAME, 'a')

    broken_links = []

    for link in links:
        href = link.get_attribute('href')
        response = requests.get(href)
        if response.status_code != 200:
            broken_links.append(href)

    return broken_links

broken_links_firefox = find_broken_links_firefox(url)

if len(broken_links_firefox) > 0:
    print('Enlaces rotos encontrados en firefox:')
    for link in broken_links_firefox:
        print(link)
else:
    print('No se encontraron enlaces rotos en firefox.')

firefox_driver.quit()
