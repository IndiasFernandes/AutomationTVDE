from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time, os, zipfile

def web_scrap_via_verde():
    """Web scrap the Via Verde website."""

    # Specify the path to the webdriver executable
    driver_path = "webdrivers/chromedriver_mac64/chromedriver"

    chrome_options = Options()

    # Get the current working directory
    cwd = os.getcwd()

    # Split the path into a list of directories
    path_list = cwd.split(os.path.sep)

    # Remove the last directory if it is "entities"
    if path_list[-1] == "entities":
        path_list = path_list[:-1]

    # Join the path back together
    new_cwd = os.path.sep.join(path_list)

    pwd_dir = new_cwd + '/downloads'
    print(os.getcwd())
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": pwd_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the website
    driver.get("https://www.viaverde.pt/empresas/")

    # Click on the input field to make it active
    elem = driver.find_element("xpath", '//*[@id="Form"]/div[3]/header/div/div[2]/div/div/ul/li[1]/button')
    elem.click()

    time.sleep(1)

    # Click on the input field to make it active
    elem = driver.find_element("xpath", '//*[@id="txtUsername"]')
    elem.send_keys('vipturismoportugal@gmail.com')

    elem = driver.find_element("xpath", '//*[@id="txtPassword"]')
    elem.send_keys('Tvpltda1=')

    elem = driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/button[2]')
    elem.click()
    time.sleep(1)

    elem = driver.find_element("xpath", '/html/body/form/div[6]/div/div/div[2]/div[1]/div[3]/button/span')
    elem.click()
    time.sleep(6)
    elem = driver.find_element("xpath", '//*[@id="Form"]/div[4]/div/div/div/div[2]/nav/ul/li[6]/a')
    elem.click()
    time.sleep(1)
    elem = driver.find_element("xpath", '//*[@id="tbExtracts"]/div/div/table/tbody/tr[1]/td[6]/div/a')
    elem.click()
    time.sleep(1)
    elem = driver.find_element("xpath", '//*[@id="tbExtracts"]/div/div/table/tbody/tr[1]/td[6]/div/div/ul/li[3]/a')
    elem.click()
    time.sleep(5)

    # # Find the submit button and click it
    #
    # # Wait for the next page to load
    # driver.implicitly_wait(5)
    #
    # submit_button = driver.find_element("xpath", '//*[@id="ember30"]')
    # print(submit_button)
    # submit_button.click()
    # # Wait for the next page to load
    # driver.implicitly_wait(5)
    #
    # submit_button = driver.find_element("xpath", '//*[@id="ember30"]')
    # print(submit_button)
    # submit_button.click()
    #
    # submit_button = driver.find_element("xpath", '//table/tbody/tr[1]/td[2]/a')
    # submit_button.click()

    time.sleep(6)

    # Close the webdriver instance
    driver.close()
def unzip_file():
    """Unzip all zip files and delete zip's of the directory 'dir_path'."""

    # Set the path to the directory containing the files
    dir_path = "../downloads"

    # Loop through all the files in the directory
    for filename in os.listdir(dir_path):

        # Check if the file is a ZIP file
        if filename.endswith(".zip"):
            # Get the full path to the ZIP file
            zip_file_path = os.path.join(dir_path, filename)

            filename = filename.replace('.zip', '.csv').upper()
            csv_file_path = os.path.join(dir_path, filename)

            # Open the ZIP file
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                # Extract the contents of the ZIP file to the same directory
                zip_ref.extractall(dir_path)

            # Delete the original ZIP file
            os.remove(zip_file_path)

            # Open the file in read mode
            with open(csv_file_path, "rb") as file:
                # Read all lines of the file
                lines = file.readlines()

            # Open the file in write mode
            with open(csv_file_path, "wb") as file:
                # Loop through all lines except the first 8
                for line in lines[8:]:
                    # Write the line to the file
                    file.write(line)

web_scrap_via_verde()
unzip_file()
