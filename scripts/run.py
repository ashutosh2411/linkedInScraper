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
#g = raw_input('Delete .data_processed?')
#u = raw_input('Delete .data_profiles?')
#c = raw_input('Delete output?')
driver = webdriver.Firefox()
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
				#sys.stdout.write("\033[F")
			except Exception:
				print ('can\'t complete ' + str(int(retry[i])))
				counter = counter + 1
				z.write(str(int(retry[i]))+'\n')
		print ('Completed with '+str(counter)+' exceptions')
		z.close()
	else:
		break
driver.quit()


counter = 0
companies = [line.rstrip('\n')for line in open('../data_source/company.txt')]

file = [f for f in listdir('../.data_profiles') if isfile(join('../.data_profiles', f))]
lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]
for x in range(len(file)):
	f = open('../.data_profiles/'+file[x],'r')
	content = f.read().split('\n')
	y = open('../.data_processed/'+file[x]+'.txt','w')
	i = 6; 
	try:	
		if(content[7]=='Company Name' or content[6]=='See more' or content[6]=='Company Name'):
			y.write('NA')
		else:	
			y.write(content[i][:-1].replace(',', ' ').replace('\"',' '))
		y.write('\n')
		y.write(content[0]	.replace(',', ' ').replace('\"',' ')+', ')
		y.write(content[3][:-1].replace(',', ' ').replace('\"',' ').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','') +', ')
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
					y.write(lines[int(file[x])][:-1]+' , ')
					flag = 1
			a=a+1
		if flag == 0:
			counter = counter + 1
			y.write('NA, '*5)
	except: 
		pass
	y.close()
print ('Files ready to be exported. Execute \"python export.py\"')


exp_file = open('../output/export.csv','w')

file = [f for f in listdir('../.data_processed')]
#lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]

for x in xrange(len(file)):
	#print x
	t = open('../.data_processed/'+str(x)+'.txt')
	y = t.readline()[:-1]+' '
	x = t.readline()+' '
	exp_file.write(x+y+'\n')
print ('Exported in /output/export.csv')
g='n'
if str(g) == 'y':
	file = [f for f in listdir('../.data_profiles') if isfile(join('../.data_profiles', f))]
	for f in file:
		os.remove('../.data_profiles/'+f)
u='n'
if str(u) == 'y':
	file = [f for f in listdir('../.data_processed') if isfile(join('../.data_processed', f))]
	for f in file:
		os.remove('../.data_processed/'+f)


#if str(g) == 'y':
file = [f for f in listdir('../.data_profiles') if isfile(join('../.data_profiles', f))]
for f in file:
	os.remove('../.data_profiles/'+f)
file = [f for f in listdir('../.data_processed') if isfile(join('../.data_processed', f))]
for f in file:
	os.remove('../.data_processed/'+f)
os.remove('geckodriver.log')