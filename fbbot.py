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
myFriend = 'myFB frie'.decode("utf-8")
myMsg = 'hello world'

# start driver
driver = webdriver.Chrome()
driver.get('https://www.facebook.com')

# wait for link to load
def loading(link):
    while driver.current_url != link:
		print 'loading link...'
		time.sleep(0.1)

# wait for element to load && to be visible
def getEl(cssSelector):
	getEl = True 
	while getEl:
		try:
			el = driver.find_element_by_css_selector(cssSelector)
			print "got element"
			while not el.is_displayed():
				pass
				print "loading element..."
			break
		except NoSuchElementException, e:
			getEl = True
	return el

# write message into non-input element
def writeMsg2el(msg, cssSelector):
	actions.move_to_element(driver.find_element_by_css_selector(cssSelector)).send_keys(msg).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

# initial login
getEl('#login_form [type="email"]').send_keys(myEmail)
getEl('#login_form [type="password"]').send_keys(myPass)
getEl('.uiButtonConfirm').click()

loginLink = 'https://www.facebook.com/'
loading(loginLink)
print 'login comleted'

# activate chat
getEl('#fbDockChatBuddylistNub').click()
print 'chat is opened'

# search and choose friend to message
getEl('#BuddylistPagelet input').send_keys(myFriend)
getEl('._29hk:first-child').click()
print 'ready to message'

# write friend
getEl('._1mf').click()
actions = ActionChains(driver)
writeMsg2el(myMsg, '._1mf')
print 'message written'