from os import listdir
from os.path import isfile, join
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