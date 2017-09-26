from os import listdir
from os.path import isfile, join

# Modify further at your own risk. 

counter = 0
companies = [line.rstrip('\n')for line in open('../data_source/company.txt')]

file = [f for f in listdir('../.data_profiles') if isfile(join('../.data_profiles', f))]
lines = [line.rstrip('\n') for line in open('../data_source/links.txt')]
for x in range(len(file)):
	f = open('../.data_profiles/'+file[x],'r')
	content = f.read().split('\n')
	#print content
	#print ''
	y = open('../.data_processed/'+file[x]+'.txt','w')
	i = 6; 
	try:	
		offset = 0
		if(content[7+offset]=='Company Name' or content[6+offset]=='See more' or content[6]=='Company Name'):
			y.write('NA')
		else:	
			y.write(content[i+offset].replace(',', ' ').replace('\"',' ').replace('\n',''))
		y.write('\n')
		y.write(content[0].replace(',', ' ').replace('\"',' ')[:-1]+', ')
		y.write(content[3+offset].replace(',', ' ').replace('\"',' ').replace('+','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')[:-1] +', ')
		
		flag = 0
		a=0
		while (a<len(content)):
			if flag==1:
				a=len(content)+1;
			if content[a] == 'Company Name': 
				if content[a+1].lower() in companies[int(file[x])].lower() or companies[int(file[x])].lower() in content[a+1].lower():
					y.write(content[a-1].replace(',',' ').replace('.',' ')+' , ')
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
					y.write(lines[int(file[x])]+' , ')
					flag = 1
			a=a+1
		if flag == 0:
			counter = counter + 1
			y.write('NA, '*5)
	except: 
		pass
	y.close()
print ('Files ready to be exported. Execute \"python export.py\"')