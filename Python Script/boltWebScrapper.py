from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# Specify the path to the webdriver executable
driver_path = "webdrivers/chromedriver_mac64/chromedriver"

chrome_options = Options()
pwd_dir = os.getcwd() + '/downloads'
print(os.getcwd())
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": pwd_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website
driver.get("https://fleets.bolt.eu/login")

# Click on the input field to make it active

elem = driver.find_element("xpath", '//*[@id="username"]')
elem.send_keys('pedro.esperanco@hotmail.com')

elem = driver.find_element("xpath", '//*[@id="password"]')
elem.send_keys('Pesp2503')




# Find the submit button and click it
submit_button = driver.find_element("xpath", '//*[@id="ember7"]')
print(submit_button)
submit_button.click()

# Wait for the next page to load
driver.implicitly_wait(5)



submit_button = driver.find_element("xpath", '//*[@id="ember30"]')
print(submit_button)
submit_button.click()
# Wait for the next page to load
driver.implicitly_wait(5)

submit_button = driver.find_element("xpath", '//*[@id="ember30"]')
print(submit_button)
submit_button.click()


submit_button = driver.find_element("xpath", '//table/tbody/tr[1]/td[2]/a')
submit_button.click()

time.sleep(60)

# Close the webdriver instance
driver.close()

