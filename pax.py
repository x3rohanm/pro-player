from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.get("https://www.feelingsurf.fr/login")
driver.find_element_by_name("login").send_keys("minamandal100@gmail.com")
driver.find_element_by_name("pass").send_keys("mina38985")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset/div[3]/button").click()
time.sleep(2)
driver.find_element_by_link_text("Earn credits").click()
time.sleep(2)
driver.find_element_by_link_text("web version").click()
time.sleep(2)
driver.find_element_by_id("toggle_surf").click()
print("...Begined...")
time.sleep(837)

driver.quit()
