from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import os
import sys
from os import listdir
from os.path import isfile, join
counter = 0
#username = driver.find_element_by_class_name("session_key-login")
#password = driver.find_element_by_class_name('password')
#username.send_keys('okabefg001@gmail.com')
#password.send_keys('Ashutosh204')
#driver.find_element_by_class_name("signin").click()
#driver.execute_script('window.open();');
#driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
g = raw_input('Delete .data_processed?')
u = raw_input('Delete .data_profiles?')
c = raw_input('Delete output?')
driver = webdriver.Firefox()
if str(g) == 'y':
	file = [f for f in listdir('../.data_profiles') if isfile(join('../.data_profiles', f))]
	for f in file:
		os.remove('../.data_profiles/'+f)
if str(u) == 'y':
	file = [f for f in listdir('../.data_processed') if isfile(join('../.data_processed', f))]
	for f in file:
		os.remove('../.data_processed/'+f)
if str(c) == 'y':
	file = [f for f in listdir('../output') if isfile(join('../output', f))]
	for f in file:
		os.remove('../output/'+f)
z=open('../output/scraping_exceptions.txt', 'w')
driver.get('https://www.linkedin.com/uas/login')
time.sleep(30)
print 'starting'
def ass (text) : return ''.join([i if ord(i) < 128 else ' ' for i in text]) 

lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]
companies = [line.rstrip('\n')for line in open('../data_source/company.txt')]
i = 0;
for i in range(len(lines)):
	#driver.execute_script('window.open();');
#	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	try:
		print ('receiving content: '+str(i))
		driver.get(lines[i])
		comp = companies[i]
		file = open('../.data_profiles/'+str(i), 'w')
		elem = driver.find_element_by_class_name("pv-top-card-section__body").text
		elem = ass(elem)
		#elem = driver.find_element_by_class_name("pv-top-card-section__summary-text").text
		#elem = ass(elem)
		file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
		time.sleep(1.25)
		elem = driver.find_element_by_class_name('experience-section').text
		elem = ass(elem)
		#print (elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' '))
		file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
			#elem = driver.find_element_by_class_name('pv-entity__extra-details').text
			#file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' '))
		file.close()
		sys.stdout.write("\033[F")
	except Exception:
		print 'can\'t complete ' + str(i)
		counter = counter + 1
		z.write(str(i)+'\n')
#	driver.execute_script('window.close();');
#	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
	#driver.close()
print 'Completed with '+str(counter)+' exceptions'
if counter == 0:
	z.write('NONE')
z.close()
driver.quit()