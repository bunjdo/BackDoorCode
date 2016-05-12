import urllib,re,base64
path = "http://localhost/urlchain/"
page = "73629254"+".html"
step = 0
def get_encoded_numbers(data, m, p):
	numbers = []
	m2=m
	while(m2):
		end = m2.end()
		#print m2.group()
		decoded_num = base64.b64decode(m2.group())
		numbers.append(decoded_num)
		data = data[end:]
		m2=p.search(data)
	return numbers

def get_numbers(data,m,p):
	numbers = []
	m2=m
	while(m2):
		end = m2.end()
		#print m2.group()
		numbers.append(m2.group())
		data = data[end:]
		m2=p.search(data)
	return numbers

while 1:
	step += 1
	print "Step "+str(step)+": "
	data = urllib.urlopen(path+page).read()
	print data
	if "DvCTF" in data:
		break
	try:
		p=re.compile('\d{5,}')
		m=p.search(data)
		numbers = get_numbers(data, m, p)
		page = numbers[0] + ".html"
		data = urllib.urlopen(path+page).read()
		while("Not Found" in data):
			numbers.pop(0)
			page = numbers[0] + ".html"
			data = urllib.urlopen(path+page).read()
		print page
	except:
		p=re.compile('[0-9a-zA-Z]{5,}=')
		m=p.search(data)
		numbers = get_encoded_numbers(data, m, p)
		page = numbers[0] + ".html"
		data = urllib.urlopen(path+page).read()
		while("Not Found" in data):
			numbers.pop(0)
			page = numbers[0] + ".html"
			data = urllib.urlopen(path+page).read()
		print page
		