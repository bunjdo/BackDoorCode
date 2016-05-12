# -*- coding: utf-8 -*-
import random, math, re, time
import socket, multiprocessing, sys

signs_alph="+-*"
brackets_alph = "()"



class ClientProcess(multiprocessing.Process):

	def __init__(self, conn, addr):
		self.steps_completed = 0
		self.conn = conn
		self.addr = addr
		self.exit = multiprocessing.Event()
		multiprocessing.Process.__init__(self)

	#только числа и +,-
	def level_1(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,2*math.pow(3,step)+10))

		#генерация знаков
		signs = []
		local_signs_alph = signs_alph[:-1] #без умножения
		for i in range(step+1):
			signs.append(random.choice(local_signs_alph))

		#составление выражения
		term = ""
		for i in range(step+1):
			term += str(numbers[i]) + " "
			term += signs[i] + " "
		term += str(numbers[-1]) + " "
		term += "=="

		#вычисление ответа
		answer = self.get_answer(term.split(" ")[:-1])
		return answer, term

	#добавим скобки
	def level_2(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,2*math.pow(3,step)+10))

		#генерация знаков
		signs = []
		local_signs_alph = signs_alph[:-1] #без умножения
		for i in range(step+1):
			signs.append(random.choice(local_signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения
		term = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term += "( "
					break
			term += str(numbers[i]) + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term += ") "
					break
			term += signs[i] + " "
		term += str(numbers[-1]) + " "
		if brackets and (brackets[-1][1] == step+2):
			term += ") "
		term += "=="

		#вычисление ответа
		answer = self.get_answer(term.split(" ")[:-1])
		return answer, term

	#добавим умножение
	def level_3(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,math.pow(3,step)+10))

		#генерация знаков
		signs = []
		for i in range(step+1):
			signs.append(random.choice(signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения
		term = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term += "( "
					break
			term += str(numbers[i]) + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term += ") "
					break
			term += signs[i] + " "
		term += str(numbers[-1]) + " "
		if brackets and (brackets[-1][1] == step+2):
			term += ") "
		term += "=="

		#вычисление ответа
		answer = self.get_answer(term.split(" ")[:-1])
		return answer, term

	#числа прописью без скобок и умножения
	def level_4(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,2*math.pow(3,step)+10))

		#перевод чисел в пропись
		str_numbers = []
		for i in range(len(numbers)):
			str_numbers.append(self.convert(numbers[i], 1))

		#генерация знаков
		signs = []
		local_signs_alph = signs_alph[:-1] #без умножения
		for i in range(step+1):
			signs.append(random.choice(local_signs_alph))

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	#числа прописью, скобки и умножение
	def level_5(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,2*math.pow(3,step)+10))

		#перевод чисел в пропись
		str_numbers = []
		for i in range(len(numbers)):
			str_numbers.append(self.convert(numbers[i], 1))

		#генерация знаков
		signs = []
		for i in range(step+1):
			signs.append(random.choice(signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term_without_convert += "( "
					term_with_convert += "( "
					break
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term_without_convert += ") "
					term_with_convert += ") "
					break
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		if brackets and (brackets[-1][1] == step+2):
			term_without_convert += ") "
			term_with_convert += ") "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	#римские числа без скобок и умножения
	def level_6(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,5*math.pow(2,step)))

		#перевод чисел в римские
		str_numbers = []
		for i in range(len(numbers)):
			str_numbers.append(self.convert(numbers[i], 2))

		#генерация знаков
		signs = []
		local_signs_alph = signs_alph[:-1] #без умножения
		for i in range(step+1):
			signs.append(random.choice(local_signs_alph))

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	#римские числа, скобки и умножение
	def level_7(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,6*math.pow(2,step)))

		#перевод чисел в римские
		str_numbers = []
		for i in range(len(numbers)):
			str_numbers.append(self.convert(numbers[i], 2))

		#генерация знаков
		signs = []
		for i in range(step+1):
			signs.append(random.choice(signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term_without_convert += "( "
					term_with_convert += "( "
					break
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term_without_convert += ") "
					term_with_convert += ") "
					break
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		if brackets and (brackets[-1][1] == step+2):
			term_without_convert += ") "
			term_with_convert += ") "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	#прописные и обычные числа, скобки и умножение
	def level_8(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,8*math.pow(3,step)))

		#перевод чисел в римские или обычные
		str_numbers = []
		for i in range(len(numbers)):
			convertmode = random.choice([0,1])
			str_numbers.append(self.convert(numbers[i], convertmode))

		#генерация знаков
		signs = []
		for i in range(step+1):
			signs.append(random.choice(signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term_without_convert += "( "
					term_with_convert += "( "
					break
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term_without_convert += ") "
					term_with_convert += ") "
					break
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		if brackets and (brackets[-1][1] == step+2):
			term_without_convert += ") "
			term_with_convert += ") "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	#римские и обычные числа, скобки и умножение
	def level_9(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,7*math.pow(2,step)))

		#перевод чисел в римские или обычные
		str_numbers = []
		for i in range(len(numbers)):
			convertmode = random.choice([0,2])
			str_numbers.append(self.convert(numbers[i], convertmode))

		#генерация знаков
		signs = []
		for i in range(step+1):
			signs.append(random.choice(signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term_without_convert += "( "
					term_with_convert += "( "
					break
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term_without_convert += ") "
					term_with_convert += ") "
					break
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		if brackets and (brackets[-1][1] == step+2):
			term_without_convert += ") "
			term_with_convert += ") "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	#римские, прописные и обычные числа, скобки и умножение
	def level_10(self, step):
		#генерация чисел
		numbers = []
		for i in range(step+2):
			numbers.append(random.randrange(1+step,8*math.pow(2,step)))

		#перевод чисел в римские или обычные
		str_numbers = []
		for i in range(len(numbers)):
			convertmode = random.choice([0,1,2])
			str_numbers.append(self.convert(numbers[i], convertmode))

		#генерация знаков
		signs = []
		for i in range(step+1):
			signs.append(random.choice(signs_alph))

		#генерация скобок
		brackets = self.generate_brackets(step)
		if brackets:
			while brackets[0][0] == 0 and brackets[0][1] == step + 2:
				brackets = self.generate_brackets(step)

		#составление выражения с конвертированными и неконвертированными числами
		term_without_convert = ""
		term_with_convert = ""
		for i in range(step+1):
			for bracket in brackets:
				if bracket[0] == i:
					term_without_convert += "( "
					term_with_convert += "( "
					break
			term_without_convert += str(numbers[i]) + " "
			term_with_convert += str_numbers[i] + " "
			for bracket in brackets:
				if bracket[1] == i+1:
					term_without_convert += ") "
					term_with_convert += ") "
					break
			term_without_convert += signs[i] + " "
			term_with_convert += signs[i] + " "
		term_without_convert += str(numbers[-1]) + " "
		term_with_convert += str_numbers[-1] + " "
		if brackets and (brackets[-1][1] == step+2):
			term_without_convert += ") "
			term_with_convert += ") "
		term_without_convert += "=="
		term_with_convert += "=="

		#вычисление ответа
		answer = self.get_answer(term_without_convert.split(" ")[:-1])
		return answer, term_with_convert

	def int2text(self, number):
	    """Converts an integer to the English language name of that integer.
	    
	    E.g. converts 1 to "One". Supports numbers 0 to 999999.
	    This can be used in LilyPond identifiers (that do not support digits).
	    
	    """
	    _nums = (
	    '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
	    'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
	    'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

	    _tens = (
	    'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty',
	    'Ninety')
	    result = []
	    if number >= 10**9:
	        billions, number = divmod(number, 10**9)
	        if number:
	            result.append(self.int2text(billions) + " " + "Billion" + " ")
	        else:
	            result.append(self.int2text(billions) + " " + "Billion")
	    
	    if number >= 10**6:
	        millions, number = divmod(number, 10**6)
	        if number:
	            result.append(self.int2text(millions) + " " + "Million" + " ")
	        else:
	            result.append(self.int2text(millions) + " " + "Million")
	    
	    if number >= 10**3:
	        hundreds, number = divmod(number, 10**3)
	        if number:
	            result.append(self.int2text(hundreds) + " " + "Thousand" + " ")
	        else:
	            result.append(self.int2text(hundreds) + " " + "Thousand")
	    
	    if number >= 100:
	        tens, number = divmod(number, 100)
	        if number:
	            result.append(_nums[tens] + " " + "Hundred" + " ")
	        else:
	            result.append(_nums[tens] + " " + "Hundred")
	    if number < 20:
	        result.append(_nums[number])
	    else:
	        tens, number = divmod(number, 10)
	        if _nums[number]:
	            result.append(_tens[tens-2] + " " + _nums[number])
	        else:
	            result.append(_tens[tens-2])
	    text = "".join(result)
	    return text or 'Zero'

	def int2roman(self, n):
	    """Convert an integer value to a roman number string.
	    
	    E.g. 1 -> "I", 12 -> "XII", 2015 -> "MMXV"
	    
	    n has to be > 1.
	    
	    """
	    _roman_numerals = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
		("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5),
		("IV", 4), ("I", 1))
	    if n < 1:
	        raise ValueError('Roman numerals must be positive integers, got %s' % n)
	    roman = []
	    for ltr, num in _roman_numerals:
	        k, n = divmod(n, num)
	        roman.append(ltr * k)
	    return "".join(roman)

	def convert(self, number, mode):
		if mode == 0:
			return str(number)
		elif mode == 1: #конвертируем число в пропись
			return self.int2text(number)
		elif mode == 2: #конвертируем число в римскую запись
			return self.int2roman(number)

	def generate_brackets(self, step):
		indexes = range(step+3)
		brackets = []
		if step > 0:
			while 1:
				begin = random.choice(indexes[:-2])
				try:
					end = random.choice(indexes[begin+2:])
				except:
					end = indexes[-1]
				brackets.append((begin,end))
				indexes = indexes[end:]
				if len(indexes) < 3:
					break
		return brackets

	def get_answer(self, term):
		#считаем выражение в скобках
		while "(" in term:
			start = term.index("(")
			end = term.index(")")
			term[start] = self.get_answer(term[start+1:end])
			del term[start+1:end+1]
		#выполняем умножение
		while "*" in term:
			index = term.index("*")
			term[index-1] = int(term[index-1])*int(term[index+1])
			del term[index:index+2]
		#складываем и вычитаем простое выражение
		result = int(term[0])
		for i in range(1,len(term),2):
			if term[i] == "+":
				result += int(term[i+1])
			elif term[i] == "-":
				result -= int(term[i+1])
		return result

	def run(self):
		self.conn.send("""Welcome to our calculating challenge.
We believe that a true IT specialist should be able to select and process any information obtained via scripts-software tricks.
You can get a lot of points, if you calculate all that will offer by server.
You have only ten sec for each answer.
Do you ready to real great processing data?
Actions available:
\t0 - Exit.
\t1 - Go.\n""")
		while not self.exit.is_set():
			try:
				data = self.conn.recv(1024)
				if data == "0\n":
					self.conn.send("Bye\n")
					self.disconnect()
				elif data == "1\n":
					self.start_game()
					self.disconnect()
				else:
					self.conn.send("No options detected.\n")
			except socket.error, msg:
				print "Error! Addr: %s. Message: %s" % (self.addr, msg)
				self.disconnect()
		return	

	def start_game(self):
		for level in range(1,11):
			for step in range(10):
				"""
				levels_dict = {1:self.level_1(step), 2:self.level_2(step), 3:self.level_3(step), 4:self.level_4(step), 
				5:self.level_5(step), 6:self.level_6(step), 7:self.level_7(step), 8:self.level_8(step), 
				9:self.level_9(step), 10:self.level_10(step)}
				"""
				answer, term = self.get_level_step(level, step)
				while answer == 0 or abs(answer) > 10**15 - 1:
					answer, term = self.get_level_step(level, step)
				self.conn.send(term)
				time.sleep(0.5)
				#отсчитываем время ответа
				time1 = time.time()
				user_answer = self.conn.recv(1024)
				time2 = time.time()
				#проверяем время ответа
				if time2-time1 >10:
					self.conn.send("Time is over :\\\n")
					return
				if user_answer.replace("\n", '') == str(answer):
					self.conn.send("True\n")
					self.steps_completed += 1
				else:
					self.conn.send("Not true, try again\n")
					return
				time.sleep(0.5)
				
				
		if self.steps_completed >= 100:
			self.get_the_flag()
		return

	def get_level_step(self, level, step):
		if level == 1:
			return self.level_1(step)
		elif level == 2:
			return self.level_2(step)
		elif level == 3:
			return self.level_3(step)
		elif level == 4:
			return self.level_4(step)
		elif level == 5:
			return self.level_5(step)
		elif level == 6:
			return self.level_6(step)
		elif level == 7:
			return self.level_7(step)
		elif level == 8:
			return self.level_8(step)
		elif level == 9:
			return self.level_9(step)
		elif level == 10:
			return self.level_10(step)
		else:
			raise socket.error
			return

	def get_the_flag(self):
		if self.steps_completed >= 100:
			congratulations = """
 _____                             _         _       _   _                 _ 
/  __ \                           | |       | |     | | (_)               | |
| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
 \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                    __/ |                                                    
                   |___/                                                     
				\n"""
			flag = """
		    	 ,----------------,              ,---------,
		    ,-----------------------,          ,"        ,"|
		  ,"                      ,"|        ,"        ,"  |
		 +-----------------------+  |      ,"        ,"    |
		 |  .-----------------.  |  |     +---------+      |
		 |  |                 |  |  |     | -==----'|      |
		 |  |  DvCTF{c@lcu    |  |  |     |         |      |
		 |  |  1aT3d_pic_Rela |  |  |/----|`---=    |      |
		 |  |  t3d}           |  |  |   ,/|==== ooo |      ;
		 |  |                 |  |  |  // |(((( [33]|    ,"
		 |  `-----------------'  |," .;'| |((((     |  ,"
		 +-----------------------+  ;;  | |         |,"
		    /_)______________(_/  //'   | +---------+
		___________________________/___  `,
	  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
	 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
	/_==__==========__==_ooo__ooo=_/'   /___________,"
	`-----------------------------'
				\n"""
			self.conn.send(congratulations)
			time.sleep(2)
			for symbol in flag:
				self.conn.send(symbol)
				time.sleep(0.02)
			print 'Got flag:', self.addr
		return

	def disconnect(self):
		print 'disconnected:', self.addr
		self.conn.close()
		self.exit.set()
		return

if __name__ == "__main__":

	try:
		HOST = sys.argv[1]
	except:
		HOST = ""

	try:
		PORT = int(sys.argv[2])
	except:
		PORT = 12345

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((HOST, PORT))
	sock.listen(2)
	print "start listening on (%s:%s) (control+C for interrupt)" % (HOST, PORT)
	while True:
		try:
			conn, addr = sock.accept()
			print 'connected:', addr
			ClientProcess(conn,addr).start()
		except KeyboardInterrupt:
			print "end listening..."
			break
		except:
			print "Error!"
			break
	sock.close()