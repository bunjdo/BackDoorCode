import re
import socket
import time

sign='+-*/'
sendnum=0
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
        "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
        "Sixteen", "Seventeen", "Eighteen", "Nineteen",
      ]

      tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

      scales = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def roman2int(numeral):
    	rlist = romanList = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
        index = 0
        intResult = 0
        for integer, romanNumeral in rlist:
            while numeral[index : index + len(romanNumeral)] == romanNumeral:
                intResult += integer
                index += len(romanNumeral)
	return intResult

def convert(s):	
	try:
		return int(s.replace(',',''))
	except:
		try:
			return text2int(s)
		except:
			return roman2int(s)

def calculate(data_list):
	while True:
                if '*' in data_list:
                        i=0
                        i=data_list.index('*')
                        data_list[i-1]=str(convert(data_list[i-1])*convert(data_list[i+1]))
                        del data_list[i:i+2]
                else:
                        break
#        print data_list
        result=convert(data_list[0])
        i=1
        for i in range(len(data_list)):
                if data_list[i] in sign:
                        if data_list[i]=='+':
                                result+=convert(data_list[i+1])
                        elif data_list[i]=='-':
                                result-=convert(data_list[i+1])
                        elif data_list[i]=='*':
                                result*=convert(data_list[i+1])
                        #elif data_list[i]=='/':
                        #        result/=float(data_list[i+1])
	return str(result)

if __name__ == "__main__":

	try:
		HOST = sys.argv[1]
	except:
		HOST = ""

	try:
		PORT = int(sys.argv[2])
	except:
		PORT = 12345

	s = socket.socket()
	s.connect((HOST, PORT))	
	data=s.recv(1024)
	print data
	s.send("1\n")
	time.sleep(1)
	while 1:
		data=s.recv(1024)
		print data
		time.sleep(0.5)
		p=re.compile('\w+'+' '+'\w+')
		data_list=data.split(' ')
		for i in range(len(data_list)):
			data_list[i]=data_list[i].replace(',','')
	#	print data_list
		p=re.compile('\w+')
		i=0
		while i != len(data_list)-1:
			if data_list[i] == '==':
				break
			m1=p.match(''.join(data_list[i]))
			m2=p.match(''.join(data_list[i+1]))
			if m1 != None and m2 != None:
				data_list[i]+= ' ' + data_list[i+1]
				del data_list[i+1]
				i-=1
	#		print data_list
			i+=1
		del data_list[-1:-2:-1]
	#	print data_list
		begin2=0
		while True:
			if '(' in data_list[begin2:]:
				i=data_list.index('(')
				i2=data_list.index(')')
				data_list[i]=calculate(data_list[i+1:i2])
				del data_list[i+1:i2+1]
	#			print data_list
				begin2=i+1
			else:
				data_list=calculate(data_list)
				break
		answer=''.join(str(data_list))
		s.send(answer+'\n')
		sendnum+=1
		print "answ: "+answer+" , step:"+str(sendnum)

		data=s.recv(1024)
		print data
		if sendnum >= 100:
			break
	while 1:
		try:
			data=s.recv(1024)
			print data,
		except:
			print "!!!end!!!"
			break
	s.close()
