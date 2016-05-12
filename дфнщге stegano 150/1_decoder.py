# -*- coding: utf-8 -*-
f = open('2.txt', 'r')
#f2 = open('2.txt', 'w')
answer = ''
for line in f.readlines():
	line = ''.join(str(line))
	#f2.write(line+'\n')
	for symb in line:
		#print unicode(symb, 'cp1251'),
		if ord(symb) not in range(20,127):
			answer+=chr(line.index(symb)+97)
			break
print answer			