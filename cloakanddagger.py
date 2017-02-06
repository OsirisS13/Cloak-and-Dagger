#this is a program to click random links on the juniper website
import pyautogui
from selenium import webdriver
from time import sleep
from random import randint

runcounter = 0
failcounter = 0
totalcounter = 0
#move the mouse in a square, because why not?
for i in range(1):
      pyautogui.moveTo(100, 100, duration=0.5)
      pyautogui.moveTo(200, 100, duration=0.1)
      pyautogui.moveTo(200, 200, duration=0.1)
      pyautogui.moveTo(100, 200, duration=0.1)
browser = webdriver.Chrome('C:\Python\Scripts\Cloak-and-Dagger\chromedriver.exe')
browser.get('http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html')
firsttab = browser.current_window_handle
#the function that chooses a link from a page
def chooselink():
	try:
		#find all links
		links = browser.find_elements_by_partial_link_text('')
		#chose a random link out of all the ones found
		l = links[randint(0, len(links)-1)]
		print (l.text)		
		print ("Trying to click: %s" %l.get_attribute("href"))
	#if there is an error (usually because there are no links on the page IE we've opened a pdf, load url of mainpage)
	except:
		#set the link as the main page
		l = 'http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html'
	#rerturn the link
	return l
	
#function that handles the clicking and checking if we want to click
def clickstuff(numbertimes):
	result = None
	#load main page
	browser.get('http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html')
	#repeat how many times specified in variable
	for i in range (numbertimes):
		#sleep to allow page to load
		sleep(1)
		print("Finish sleep")
		sleep(1)
		#run chooselink function		
		l = chooselink()
		#check to see if the link chosen was a social link, and if it was then ignore it and run function again
		if l == 'http://www.facebook.com/JuniperNetworks/':
			l = 'http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html'
		elif l == 'http://twitter.com/JuniperNetworks/':
			l = 'http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html'
		elif l == 'http://www.youtube.com/junipernetworks':
			l = 'http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html'
		elif l == 'https://www.linkedin.com/company/juniper-networks':
			l = 'http://www.juniper.net/techpubs/en_US/junos-space13.3/index.html'
		else:
			while result is None:
				sleep(0.5)
				try:
					#click link				
					l.click()
					result = True
					#increase run counter
				#	runcounter = runcounter + 1
				#if for some reason it doesnt work, generate another link to click
				except:
					print("hit an error")
					sleep(0.5)
					#select focus to first tab (usually because weve clicked something that opens new tab)
					browser.switch_to_window(firsttab)
					l = chooselink()
					#increase fail counter
					#failcounter = failcounter + 1
		#wait some random time between 10 and 120 secs
		sleepytime = randint(15,120)
		print("Done, sleeping for %s seconds" %sleepytime)
		sleep(sleepytime)
		result = None
		#totalcounter = totalcounter + 1

for i in range (1,20):
	clickstuff(20)
	print("Finished run 1")
	clickstuff(20)
	print("Finished run 2")
	clickstuff(20)
	print("Finished run 3")
	clickstuff(20)
print("Finished job")
#print ("Clicked successfully %s times" %runcounter)
#print ("Click failed %s times" %failcounter)
#print ("Total clicks %s" %totalcounter)
#successrate = runcounter / totalcounter * 100
#print ("Click success rate is %s%" %successrate)

browser.close()
print("Browser closed")

