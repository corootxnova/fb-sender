# -*- coding: utf-8 -*-
try:
	from selenium import webdriver
	from time import sleep
	from colored import fg, attr

except:
	print(' >>> Install Selenium And Colored > pip install selenium - pip install colored')
	sleep(15)

import os
os.system("title Messenger Sender V0.1")

print('''

d88888b d8888b.        .d8888. d88888b d8b   db d8888b. d88888b d8888b. 
88'     88  `8D        88'  YP 88'     888o  88 88  `8D 88'     88  `8D 
88ooo   88oooY'        `8bo.   88ooooo 88V8o 88 88   88 88ooooo 88oobY' 
88~~~   88~~~b. C8888D   `Y8b. 88~~~~~ 88 V8o88 88   88 88~~~~~ 88`8b   
88      88   8D        db   8D 88.     88  V888 88  .8D 88.     88 `88. 
YP      Y8888P'        `8888Y' Y88888P VP   V8P Y8888D' Y88888P 88   YD 
                                                                        
                                                                        

''')
username = input(fg('yellow_4b') + " >>> Enter Sender Email Here : ")
password = input(fg('yellow_4b') + " >>> Enter Sender Pass Here : ")
delay = int(input(fg('yellow_4b') + " >>> Enter Delay : "))
upload = input(fg('yellow_4b') + " >>> Upload ID/Username List : ")
upload_msg = input(fg('yellow_4b') + " >>> Enter Message Text File : ")
ids = open(upload, 'r')
message = open(upload_msg, 'r', encoding='utf-8').read()
ok = '\n'
driver = webdriver.Chrome()
driver.get("https://www.messenger.com/login")
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
sleep(2)
for _id in ids:
	driver.get("https://www.messenger.com/t/" + _id)
	sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div/div/div").send_keys(message + ok)
	print(fg('dark_cyan') + " >>> Sent Successfully To " + _id + attr("reset"))
	sleep(int(delay))
	driver.quit()
