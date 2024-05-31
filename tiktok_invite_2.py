import time
import csv
import pyautogui
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd

# Load the list of usernames from the provided CSV file
def load_usernames(csv_file):
    usernames = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            usernames.append(row[0])
    return usernames

# Initialize the Selenium WebDriver
def init_driver():
    driver = webdriver.Chrome()  # Ensure the path to chromedriver is in your PATH
    driver.maximize_window()
    driver.get("https://seller-us-accounts.tiktok.com/account/login")
    return driver

# Perform login (manual step due to Captcha and 2fa)
def login(driver):
    print("Please log in manually to bypass Captcha and 2fa.")
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sc_menu_container"]/div/div/a[2]'))
    )
    print("Login Successful!")
    
def gotoInvitePage(driver, counter):
    pyautogui.sleep(2)
    if(counter == 0):
        driver.get("https://affiliate-us.tiktok.com/connection/target-invitation?source_from=seller_affiliate_landing&shop_region=US&tab=1")
        driver.execute_script("window.localStorage.setItem('ecom-seller-target-invitation-sample-feature-guide-entry-7495783518239623446', 'true');")
        driver.execute_script("window.localStorage.setItem('ecom-seller-target-invitation-feature-guide-modal-7495783518239623446', 'true');")
        driver.execute_script("window.localStorage.setItem('ecom-seller-guide--revamp-plan-modal-guide-new_7495783518239623446', 'visited');")
        driver.execute_script('window.localStorage.setItem(''"ecom-seller-guide--revamp-plan-menu-guide-new_7495783518239623446", ''"[\'open_collaboration\',\'targeted_collaboration\']");')
    pyautogui.sleep(2)
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/div[2]/button'))
    )
    element = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/div[2]/button')
    element.click()

    

# Function to send a target collaboration invitation
def addUsers(driver, username, message):
    try:
        WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/span/span/input'))
        )
        search_box = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/span/span/input')
        actions=ActionChains(driver)
        actions.click(search_box)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE)
        actions.perform()
        search_box.send_keys(f'{username}')
        user_icon_coordinates = (351, 450) 
        pyautogui.moveTo(user_icon_coordinates[0], user_icon_coordinates[1], duration=1)
        pyautogui.click()
        pyautogui.sleep(2)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"{username}: Error - {str(e)}")

def fillForm(driver, counter, email):
    try:
        i = '3'
        WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/div'))
        )
        element = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/div')
        pyautogui.sleep(2)
        element.click()
        pyautogui.sleep(2)
        WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/table/tbody/tr/td/div/div/button'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element = driver.find_element(By.XPATH,'//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/table/tbody/tr/td/div/div/button')
        element.click()        
        WebDriverWait(driver, 300).until(           
        EC.presence_of_element_located((By.XPATH, f'/html/body/div[{i if counter == 0 else '4'}]/div[2]/div/span/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/table/tbody/tr[1]/td[1]/label/span/div'))
        )               
        checkbox = driver.find_element(By.XPATH, f'/html/body/div[{i if counter == 0 else '4'}]/div[2]/div/span/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/table/tbody/tr[1]/td[1]/label/span/div')
        checkbox.click()
        addBtn = driver.find_element(By.XPATH, f'/html/body/div[{i if counter == 0 else '4'}]/div[2]/div/span/div/div[3]/div/div/div[2]/button[2]')
        addBtn.click()
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div[3]/table/tbody/tr/td[6]/div/span/div/div/div/div/div/div/div/span/span/input')))
        commisionBox = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div[3]/table/tbody/tr/td[6]/div/span/div/div/div/div/div/div/div/span/span/input')
        commisionBox.send_keys("30")
        setUpSamples = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div')
        setUpSamples.click()
        pyautogui.sleep(2)
        WebDriverWait(driver, 300).until(          
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/button'))
        )
        sampleBtn = driver.find_element(By.XPATH,'//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/button')
        driver.execute_script("arguments[0].scrollIntoView(true);", setUpSamples)
        WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/button'))
        )
        sampleBtn.click()
        
        WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[1]/div'))
        )
        createInvitation = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[1]/div')
        createInvitation.click()
        WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="target_complete_details_name"]/div/div/span/span/input'))
        )
        inviteName = driver.find_element(By.XPATH,'//*[@id="target_complete_details_name"]/div/div/span/span/input')
        driver.execute_script("arguments[0].scrollIntoView(true);", inviteName)
        inviteName.send_keys("Livfresh x TikTok Shop")
        
        messageBox = driver.find_element(By.XPATH,'//*[@id="target_complete_details_message_input"]')
        actions=ActionChains(driver)
        actions.click(messageBox)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE)
        actions.perform()
        messageBox.send_keys(message)

        emailAddress = driver.find_element(By.XPATH,'//*[@id="target_complete_details_contacts_7_input"]')
        actions=ActionChains(driver)
        actions.click(emailAddress)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE)
        actions.perform()
        emailAddress.send_keys(email)
        
        pyautogui.sleep(2)

        validUntil = driver.find_element(By.XPATH,'//*[@id="target_complete_details_until"]/div/div/div[1]/input')
        validUntil.send_keys("006/30/2024")
        
        # pyautogui.sleep(8)

        validUntil.send_keys(Keys.ENTER)

    
        
        # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, 'asd')))
       
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error - {str(e)}")


def preAddUserSectionOpen(driver):
    
    pyautogui.scroll(10000)
    pyautogui.sleep(2)
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div'))
        )
    addUserCollapsible = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div')
    addUserCollapsible.click()



def submit(driver):
    pyautogui.scroll(-10000)
    pyautogui.sleep(5)
    sendBtn = driver.find_element(By.XPATH,'//*[@id="content-container"]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[2]/button[2]')
    sendBtn.click()
    pyautogui.sleep(5)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/div[2]/div/img'))
        )
        print("Batch successful")
    except NoSuchElementException:
        print("Batch unsuccessful")

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/div[2]/div/button'))
        )
    viewInvitations = driver.find_element(By.XPATH, '//*[@id="content-container"]/main/div/div/div/div/div[2]/div/div[2]/div/button')
    viewInvitations.click()


def main(usernames, message, email):
    batch_size = 50

    driver = init_driver()
    login(driver)
    # gotoInvitePage(driver)
    
    # Split usernames into batches
    for i in range(0, len(usernames), batch_size):
        gotoInvitePage(driver,i)
        usernames_batch = usernames[i:i+batch_size]
        
        fillForm(driver, i, email)
        preAddUserSectionOpen(driver)
        
        for username in usernames_batch:
            addUsers(driver, username, message)

        submit(driver)
        
    driver.quit()

if __name__ == "__main__":
    usernames = load_usernames("username_4.csv")
    message = 'Hey! Would love to send our non-fluoride toothpaste that has been clinically proven to remove plaque and heals gum 100%+ better! Please request the 1 tube option!'
    email = "target@joinspotlight.org"
    
    main(usernames, message, email)
