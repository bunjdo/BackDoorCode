import os
import random as r
import base64 as b

#debug
recreate = 1

#global
count  = 250
folder = 'urlchain'
numbers = []

#functions
def create_folder(folder):
	return os.system("mkdir "+folder)

def parse_lvl1(number):
	content = "You found it! Next number is "+str(number)+".";
	return content

def parse_lvl2(number):
	fake_nums = []
	for i in range(3):
		num = r.randint(10000000, 99999999)
		while(num in numbers):
			num = r.randint(10000000, 99999999)
		fake_nums.append(num)
	fake_nums.append(str(number))
	r.shuffle(fake_nums)

	content = "Next number is one of these: "+str(fake_nums[0])+', '+str(fake_nums[1])+', or these: '+str(fake_nums[2])+', '+str(fake_nums[3])+"."
	return content	

def parse_lvl3(number):
	fake_nums = []
	for i in range(3):
		num = r.randint(10000000, 99999999)
		while(num in numbers):
			num = r.randint(10000000, 99999999)
		fake_nums.append(num)
	fake_nums.append(str(number))
	r.shuffle(fake_nums)

	for index, number in enumerate(fake_nums):
		fake_nums[index] = b.b64encode(str(number))

	content = "The last steps on the way: "+str(fake_nums[0])+', '+str(fake_nums[1])+', '+str(fake_nums[2])+', '+str(fake_nums[3])+". Choose correct and follow this."
	return content

def flag_bitch():
	return 'DvCTF{g3t_Wh@t_y0u_de\$eRv3}'

def first_page(number):
	content = 'You have a good opportunity to get some points for your team. For continue, try  '+str(number)+'.'
	return content	

def generate():
	while len(numbers)<count:
		number = r.randint(10000000, 99999999)
		if number not in numbers:
			numbers.append(number)
	for index, number in enumerate(numbers):
		filename = folder+"/"+str(number)+".html"
		#parse levels logic
		if index==count-1:
			content = flag_bitch()
			print "Last page: "+str(number)
		elif index==1:
			content = first_page(numbers[index+1])
			print "First page: "+str(number)
		elif index<=(2*count/5):
			content = parse_lvl1(numbers[index+1])
		elif index>(2*count/5) and index<=(4*count/5):
			content = parse_lvl2(numbers[index+1])
		elif index>(4*count/5):
			content = parse_lvl3(numbers[index+1])
		##
		os.system("touch "+filename)
		os.system("echo "+content+" > "+filename)
		if index == 10:
			print "Step 10: "+str(number)
		if index == 55:
			print "Step 55: "+str(number)
		if index == 175:
			print "Step 175: "+str(number)

cr_folder = create_folder(folder)
if not cr_folder:
	generate()
else:
	if recreate:
		os.system("rm -r "+folder)
		create_folder(folder)
		generate()
	else:
		print cr_folder