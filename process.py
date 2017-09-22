from os import listdir
from os.path import isfile, join

companies = [line.rstrip('\n')for line in open('company.txt')]

file = [f for f in listdir('data') if isfile(join('data', f))]
lines = [line.rstrip('\n') for line in open('links.txt')]

for x in range(len(file)):
	#print companies[x]
	print x, file[x]
	f = open('data/'+file[x],'r')
	content = f.read().split('\n')
	y = open('data_processed/'+file[x]+'.txt','w')
	i = 6; 
	#if not (content[i] == 'See more' or content[i+1] == 'Company Name'):
	try:	
		if(content[7]=='Company Name' or content[6]=='See more'):
			y.write('NA')
		else:	
			y.write(content[i].replace(',', ' ').replace('\"',' '))
		y.write('\n')
		y.write(content[0].replace(',', ' ').replace('\"',' ')+', ')
		y.write(content[3].replace(',', ' ').replace('\"',' ') +', ')
		flag = 0
		a=0
		while (a<len(content)):
			if flag==1:
				a=len(content)+1;
			if content[a] == 'Company Name': 
				if content[a+1].lower() in companies[int(file[x])].lower() or companies[int(file[x])].lower() in content[a+1].lower():
					try:
						y.write(content[a-1].replace(',',' ')+' , ')
					except:
						y.write('NA, ')
					try:
						y.write(content[a+1].replace(',',' ')+' , ')
					except:
						y.write('NA, ')
					try:
						y.write(content[a+3].replace(',',' ')+' , ')
					except:
						y.write('NA, ')
					try:
						y.write(content[a+5].replace(',',' ')+' , ')
					except:
						y.write('NA, ', )
					#y.write(companies[int(file[x])].replace(',', ' ').replace('\"',' ')+', ')
					y.write(lines[x]+' , ')
					print('done')
					flag = 1
			a=a+1
	except: 
		pass
	
	#print '++++++++++++++++++++++++++++++++++++++++++++++++++'