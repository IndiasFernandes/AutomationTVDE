from selenium.webdriver.chrome.options import Options
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the webdriver executable
driver_path = "webdrivers/chromedriver_mac64/chromedriver"

o = webdriver.ChromeOptions()
o.add_argument = {'user-data-dir':'/Users/Application/Chrome/Default'}

chrome_options = Options()
pwd_dir = os.getcwd() + '/downloads'
print(os.getcwd())
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": pwd_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Setup wait for later
wait = WebDriverWait(driver, 10)

# Navigate to the website
driver.get("https://www.uber.com/global/en/sign-in/")

# Get original window tab
original_window = driver.current_window_handle

# Click on the Driver Button
submit_button = driver.find_element("xpath", '//*[@id="animation-wrapper"]/a/div/div/div[1]/div/h2')
submit_button.click()

# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        print(f'switched to {window_handle}')
        break

driver.implicitly_wait(5)

elem = driver.find_element("xpath", '//*[@id="PHONE_NUMBER_or_EMAIL_ADDRESS"]')
elem.send_keys('vogaisportugal@gmail.com')

elem = driver.find_element("xpath", '//*[@id="forward-button"]')
elem.click()

driver.implicitly_wait(4)
elem = driver.find_element("xpath", '//*[@id="back-button"]')
elem.click()

driver.implicitly_wait(4)
elem = driver.find_element("xpath", '//*[@id="forward-button"]')
elem.click()


# Wait for the next page to load
driver.implicitly_wait(4)
time.sleep(10)

elem = driver.find_element("xpath", '//*[@id="PASSWORD"]')
elem.send_keys('12ariano3')
elem = driver.find_element("xpath", '//*[@id="forward-button"]')

# Wait for the next page to load
driver.implicitly_wait(10)
time.sleep(10)

elem = driver.find_element("xpath", '//*[@id="wrapper"]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[5]/span')
elem.click()


elem = driver.find_element("xpath", '//*[@id="wrapper"]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div[1]')
elem.click()

elem = driver.find_element("xpath", '//*[@id="bui364val-2"]')
elem.click()

elem = driver.find_element("xpath", '//*[@id="wrapper"]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/input')
elem.send_keys('2023/03/13 – 2023/03/19')

elem = driver.find_element("xpath", '//*[@id="wrapper"]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/button')
elem.click()

time.sleep(10)
elem = driver.find_element("xpath", '//*[@id="wrapper"]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[5]/div/div/div/button/svg')
elem.click()


time.sleep(100)

# Close the webdriver instance
driver.close()

