

f = open('nameslist.txt','r')
list = []
tp = []
final = []
for line in f.readlines():

	 list.append(line.split(' '))
for x in list:
	#print x
	final.append(x[2])
	
	'''
	if x.isdigit():
		tp.append(x)
	else:
		final.append(x)
	'''
#print list
print final
