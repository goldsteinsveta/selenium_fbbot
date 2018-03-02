#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# login details
myEmail = 'myFB@email.net'
myPass = 'myFBpassword'

# search for friend string, must not contain the whole name
myFriend = 'Sveta Goldstein'.decode("utf-8")
myMsg = 'hello world'

# start driver
driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)



driver.get('https://www.facebook.com')

# wait for link to load
def loading(link):
	print 'loading page...'
	while driver.current_url != link:
		time.sleep(0.1)

# wait for element to load && to be visible
def getEl(cssSelector):
	getEl = True
	print "looking for a button"
	while getEl:	
		try:
			el = driver.find_element_by_css_selector(cssSelector)
			print "got it!"
			while not el.is_displayed():
				pass
			break
		except NoSuchElementException, e:
			getEl = True
	return el

# write message into non-input element
actions = ActionChains(driver)

def writeMsg2el(msg, cssSelector):
	actions.move_to_element(driver.find_element_by_css_selector(cssSelector)).send_keys(msg).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

# initial login
getEl('#login_form [type="email"]').send_keys(myEmail)
getEl('#login_form [type="password"]').send_keys(myPass)
getEl('.uiButtonConfirm').click()

loginLink = 'https://www.facebook.com/'
# loading(loginLink)
print 'login comlete'

# notification popup
# getEl('.uiLayer .uiOverlayFooter a.layerCancel').click()

# activate chat
print 'openeing the chat'
getEl('#fbDockChatBuddylistNub').click()

# search and choose friend to message
print 'looking for a friend'
getEl('#BuddylistPagelet input').send_keys(myFriend)
getEl('._29hk:first-child').click()
print 'found!'

# write friend
getEl('._1mf').click()
writeMsg2el(myMsg, '._1mf')
print 'message is written'