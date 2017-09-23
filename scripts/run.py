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
#g = raw_input('Delete data_processed?')
#u = raw_input('Delete data_profiles?')
#c = raw_input('Delete output?')
g = 'y'
u = 'y'
c = 'y'
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


counter = 0
companies = [line.rstrip('\n')for line in open('../data_source/company.txt')]

file = [f for f in listdir('../.data_profiles') if isfile(join('../.data_profiles', f))]
lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]
z=open('../output/manual_check.txt','w')
for x in range(len(file)):
	#print companies[x]
	#print x, file[x]
	f = open('../.data_profiles/'+file[x],'r')
	content = f.read().split('\n')
	y = open('../.data_processed/'+file[x]+'.txt','w')
	i = 6; 
	#if not (content[i] == 'See more' or content[i+1] == 'Company Name'):
	try:	
		if(content[7]=='Company Name' or content[6]=='See more' or content[6]=='Company Name'):
			y.write('NA')
		else:	
			y.write(content[i].replace(',', ' ').replace('\"',' '))
		y.write('\n')
		y.write(content[0].replace(',', ' ').replace('\"',' ')+', ')
		y.write(content[3].replace(',', ' ').replace('\"',' ').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','') +', ')
		flag = 0
		a=0
		while (a<len(content)):
			if flag==1:
				a=len(content)+1;
			if content[a] == 'Company Name': 
				if content[a+1].lower() in companies[int(file[x])].lower() or companies[int(file[x])].lower() in content[a+1].lower():
					try:
						y.write(content[a-1].replace(',',' ').replace('.',' ')+' , ')
					except:
						y.write('NA, ')
					try:
						y.write(content[a+1].replace(',','').replace('.',' ')+' , ')
					except:
						y.write('NA, ')
					try:
						w = content[a+3].replace(',',' ').replace('.',' ')
						if w == 'Company Name':
							w = 'NA'
						if w[0].isdigit():
							w = w[0:4]+' - '+w[7:]
						else:
							w = w[0:8]+' - '+w[11:]
						y.write(w+' , ')
					except:
						y.write('NA, ')
					try:
						y.write(content[a+5].replace(',',' ').replace('.',' ')+' , ')
					except:
						y.write('NA, ', )
					#y.write(companies[int(file[x])].replace(',', ' ').replace('\"',' ')+', ')
					y.write(lines[x]+' , ')
					#print('done')
					flag = 1
			a=a+1
		if flag == 0:
			#print '------------'+file[x]
			counter = counter + 1
			z.write(file[x]+'\n')
			y.write('NA, '*5)
	except: 
		pass
	y.close()
if counter == 0:
	z.write('NONE')
z.close()
print 'no of manual checks to be done: '+str(counter)
	#print '++++++++++++++++++++++++++++++++++++++++++++++++++'


exp_file = open('../output/export.csv','w')

file = [f for f in listdir('../.data_processed')]
lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]

for x in xrange(len(file)):
	#print x
	t = open('../.data_processed/'+str(x)+'.txt')
	y = t.readline()[:-1]+' '
	x = t.readline()+' '
	exp_file.write(x+y+'\n')
print 'Exported in /output/export.csv'