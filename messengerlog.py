
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip
import sys

if len(sys.argv) > 1:
    profile = " USERNAME".join(sys.argv[1:])
    print(profile)
else:
    profile = "USERNAME"

# Code nabbed from Stack Overflow to disable 
# notifications for selenium
b = webdriver.Firefox()
b.get('http://facebook.com')

email = b.find_element_by_css_selector("#email")
password = b.find_element_by_css_selector("#pass")

email.send_keys("USERNAME")
password.send_keys("PASSWORD")

password.submit()

## Send status automatically ##
messages = b.find_element_by_css_selector("a[data-testid='left_nav_item_Messages']")
messages.click()

try:
    newMessage = WebDriverWait(b, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button._3mv"))
    )
    newMessage.click()
except:
    b.quit()

try:
    search = WebDriverWait(b, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.inputtext.textInput"))
    )
    search.click()
    search.send_keys(profile)
    search.send_keys(Keys.ENTER)
except:
    b.quit()

messageToSend = b.find_element_by_tag_name("textarea")
messageToSend.click()

messageToSend.send_keys("Hey, " + profile.split()[0] + ". This message was programmatically generated. Just ignore it. Thanks for playing :-)")
messageToSend.send_keys(Keys.RETURN)
##thank stackeoverflow
Contact GitHub API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Status Help
