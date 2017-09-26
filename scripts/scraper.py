from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import os
import sys
from os import listdir
from os.path import isfile, join

# all modifications to be done in following lines

# wait for user to input login credentials
# set to >=5 if you want to signal login success by 'pressing any key'
LOGIN_TIME 		= 30

# wait before loading next page in general
WAIT_GENERAL 	= .75

# wait before loading next in case of exception, which may be due to connectivity issues
WAIT_EXCEPTION	= 3

# Modify further codec section at your own risk
counter = 0
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
z=open('../output/scraping_exceptions.txt', 'w+')
driver.get('https://www.linkedin.com/uas/login')
if (LOGIN_TIME > 5):
	time.sleep(LOGIN_TIME-5)
	print ('starting')
	time.sleep(5)
else:
	raw_input('Press any key to continue... ')
	print ('starting')
def ass (text) : return ''.join([i if ord(i) < 128 else ' ' for i in text]) 

lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]
companies = [line.rstrip('\n')for line in open('../data_source/company.txt')]
i = 0;
for i in range(len(lines)):
	try:
		sys.stdout.write('\r')
		sys.stdout.flush()
		print ('receiving content: '+str(i))
		driver.get(lines[i])
		time.sleep(WAIT_GENERAL)
		comp = companies[i]
		file = open('../.data_profiles/'+str(i), 'w')
		try:
			elem = driver.find_element_by_class_name("pv-top-card-section__body").text
			elem = ass(elem)
			file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
		except:
			driver.get(lines[i])
			time.sleep(WAIT_EXCEPTION)
			elem = driver.find_element_by_class_name("pv-top-card-section__body").text
			elem = ass(elem)
			file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
		try:
			elem = driver.find_element_by_class_name('experience-section').text
			elem = ass(elem)
			file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
		except:
			driver.get(lines[i])
			time.sleep(WAIT_EXCEPTION)
			elem = driver.find_element_by_class_name('experience-section').text
			elem = ass(elem)
			file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
		file.close()
	except Exception:
		print ('can\'t complete ' + str(i))
		counter = counter + 1
		z.write(str(i)+'\n')
print ('Completed with '+str(counter)+' exceptions')
if counter == 0:
	z.write('NONE')
z.close()
while 1==1:
	
	choice = 'n'
	if not counter ==0:
		choice = raw_input('would you like to retry exceptions?')
	else:
		pass
	if(choice == 'y'):
		counter = 0
		exception = open('../output/scraping_exceptions.txt','r')
		retry = exception.read().split()
		exception.close()
		os.remove('../output/scraping_exceptions.txt')
		z=open('../output/scraping_exceptions.txt', 'w+')
		print (retry)
		for i in range(len(retry)):
			try:
				print ('receiving content: '+str(int(retry[i])))
				driver.get(lines[int(int(retry[i]))])
				time.sleep(WAIT_EXCEPTION)
				comp = companies[int(retry[i])]
				file = open('../.data_profiles/'+str(int(retry[i])), 'w')
				elem = driver.find_element_by_class_name("pv-top-card-section__body").text
				elem = ass(elem)
				file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
				elem = driver.find_element_by_class_name('experience-section').text
				elem = ass(elem)
				file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
				file.close()
				sys.stdout.write("\033[F")
			except Exception:
				print ('can\'t complete ' + str(int(retry[i])))
				counter = counter + 1
				z.write(str(int(retry[i]))+'\n')
		print ('Completed with '+str(counter)+' exceptions')
		z.close()
	else:
		break
driver.quit()