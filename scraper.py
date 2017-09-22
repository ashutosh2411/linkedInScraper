from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/uas/login')
#username = driver.find_element_by_class_name("session_key-login")
#password = driver.find_element_by_class_name('password')
#username.send_keys('okabefg001@gmail.com')
#password.send_keys('Ashutosh204')
#driver.find_element_by_class_name("signin").click()
#driver.execute_script('window.open();');
#driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
time.sleep(20)
print 'starting'
def ass (text) : return ''.join([i if ord(i) < 128 else ' ' for i in text]) 

lines = [line.rstrip('\n') for line in open('links.txt')]
companies = [line.rstrip('\n')for line in open('company.txt')]
i = 0;
for i in range(98,len(lines)):
	#driver.execute_script('window.open();');
#	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	try:
		driver.get(lines[i])
		comp = companies[i]
		file = open('data/'+str(i), 'w')
		elem = driver.find_element_by_class_name("pv-top-card-section__body").text
		elem = ass(elem)
		#elem = driver.find_element_by_class_name("pv-top-card-section__summary-text").text
		#elem = ass(elem)
		file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
		time.sleep(2.5)
		elem = driver.find_element_by_class_name('experience-section').text
		elem = ass(elem)
		#print (elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' '))
		file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' ').replace(u'\u2013', ' '))
			#elem = driver.find_element_by_class_name('pv-entity__extra-details').text
			#file.write(elem.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u2022', ' '))
		file.close()
		print 'done number '+ str(i)
	except Exception:
		print 'can\'t open ' + str(i)
#	driver.execute_script('window.close();');
#	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
	#driver.close()
driver.quit()