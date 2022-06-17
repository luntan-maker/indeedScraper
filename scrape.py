from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

import random

import pandas as pd


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.indeed.com")
# Set headers?
# https://pypi.org/project/selenium-stealth/

def startIndeedPage(search_term="developer"):
    elem = driver.find_element(By.NAME, "q")
    time.sleep(1)
    elem.send_keys(search_term)
    # time.sleep(1)
    
    elem2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'l')))
    elem2.click()
    # elem2.clear()
    for i in range(20):
        elem2.send_keys(Keys.BACKSPACE)
    elem2.send_keys("remote")
    time.sleep(3)
    elem2.send_keys(Keys.RETURN)

def scrapePages(jobPages=5):
    df = pd.DataFrame(columns=['data'])
    for i in range(jobPages):
        try:
            jobs = driver.find_elements(By.CLASS_NAME, "jobTitle")
            # Randomize the process
            print(type(jobs))
            random.shuffle(jobs)
            for i in jobs:
                i.click()
                # Random sleeping
                time.sleep(random.randrange(3, 5))
                # Move more
                ActionChains(driver).move_to_element_with_offset(i, 8,11).perform()
                frame = driver.find_element_by_tag_name("iframe")
                driver.switch_to.frame(frame)
                text = driver.find_element(By.ID, "jobDescriptionText")
                print(text.text)
                
                df = df.append({'data':text.text}, ignore_index=True)

                driver.switch_to.default_content()
            
            # next = driver.find_element(By.CLASS_NAME, "np")
            # next.click()
            # Check for popup
            # close = driver.find_element_(By.CLASS_NAME, "popover-x-button-close icl-CloseButton")
            # close.click()

        except NoSuchElementException:
            print("Something's not there, breaking from the loop")
    return df

from datetime import datetime

pages = 1
search_term = "developer"
now = datetime.now()
startIndeedPage(search_term)
df = scrapePages(pages)
df.to_csv("./"+str(pages)+"_"+search_term+"_"+now.strftime("%d_%m_%Y %H_%M_%S"))

# https://groups.google.com/g/selenium-users/c/W4s7KJbsEzc?pli=1
# https://github.com/abhinavsingh/proxy.py
# https://www.us-proxy.org/
# https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en
# https://stackoverflow.com/questions/34222412/load-chrome-extension-using-selenium
# https://www.reddit.com/r/webscraping/comments/uxuleb/deploying_an_indeedcom_scraper_to_aws_lambdaec2/ia1uah9/
# https://aws.amazon.com/blogs/architecture/serverless-architecture-for-a-structured-data-mining-solution/
# https://aws.amazon.com/blogs/architecture/serverless-architecture-for-a-web-scraping-solution/
# https://aws.amazon.com/blogs/architecture/emerging-solutions-for-operations-research-on-aws/

# https://stackoverflow.com/questions/7263824/get-html-source-of-webelement-in-selenium-webdriver-using-python


