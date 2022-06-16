from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.indeed.com")

def startIndeedPage(search_term="developer"):
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(search_term)
    
    elem2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'l')))
    elem2.click()
    # elem2.clear()
    for i in range(20):
        elem2.send_keys(Keys.BACKSPACE)
    elem2.send_keys("remote")
    elem2.send_keys(Keys.RETURN)



startIndeedPage()
# driver.close()

jobs = driver.find_elements(By.CLASS_NAME, "jobTitle")
# jobs = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'jobTitle')))

for i in jobs:
    # if "new" not in i.text:
    i.click()
    time.sleep(3)
    ActionChains(driver).move_to_element_with_offset(i, 8,11).perform()
    # print(i.text)
    # text = driver.find_element(By.CLASS_NAME, "jobsearch-jobDescriptionText")
    # text = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'jobsearch-jobDescriptionText')))#driver.find_element(By.ID, "jobDescriptionText")
    # text = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'vjs-container-iframe')))#driver.find_element(By.ID, "jobDescriptionText")
    frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(frame)
    text = driver.find_element(By.ID, "jobDescriptionText")
    print(text.text)
    driver.switch_to.default_content()
        # text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded')))#driver.find_element(By.ID, "jobDescriptionText")
        # print(text)icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded
next = driver.find_element(By.CLASS_NAME, "np")
next.click()
close = driver.find_element(By.CLASS_NAME, "popover-x-button-close icl-CloseButton")
close.click()
# for j in arr:
        
    # Click on each one
    # Wait for loading
        # Look for className: icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded
    # Get all data from id: jobDescriptionText
# Throw data into pandas frame
# Paginate
# Repeat until next page is gone or disabled
# 
# driver.close()