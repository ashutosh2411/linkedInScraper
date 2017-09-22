from os import listdir
from os.path import isfile, join

exp_file = open('export.csv','w')

file = [f for f in listdir('data_processed')]
lines = [line.rstrip('\n') for line in open('links.txt')]

for x in xrange(len(file)):
	print x
	t = open('data_processed/'+str(x)+'.txt')
	y = t.readline()[:-1]+' '
	x = t.readline()+' '
	exp_file.write(x+y+'\n')