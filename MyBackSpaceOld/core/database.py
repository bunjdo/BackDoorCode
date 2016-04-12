import sqlite3

class Database:
	"""Usage:
	insert_into(table_name).values(tuple).run():
		inserts tuple into table table_name
		equvalent for row SQL "INSERT INTO table_name VALUES tuple;"
		tuple may be one tuple like (..., ..., ...) or list of tuples like [(...),(...),(...),...]
		Warning!!! Commit your changes after inserting!
	select(table_name).run():
		selects all information from table table_name
		equvalent for row SQL "SELECT * FROM table_name;"
	"""

	__path_ = ''
	__db_ = None
	__cursor_ = None
	__select_query_ = None
	__insert_into_tablename_ = None

	def __init__(self, path):
		self.__path_ = path
		self.__init_db_()

	def run_sql(self, sql_string):
		""""Unsafe!!!! execute exact sql_string SQL-Code, no extra checking performed"""
		print('Executing SQL "' + sql_string + '"')
		self.__db_.execute(sql_string)
		self.__db_.commit()

	def insert_into(self, table_name):
		"""Set table name for insertion values
		Usage: db_instanse.insert_into(table_name).values(var_tuple)"""
		self.__insert_into_tablename_ = table_name
		return self

	def values(self, var_tuple):
		""""var_tuple is tuple of variables like (..., ..., ...)
		or list of tuples like [(...),(...),(...),...]
		length of tuple or each tuple in list is the same with
		number of colums in __insert_into_tablename_ table
		Warning!!! Commit your changes after inserting!"""
		if self.__insert_into_tablename_ == None:
			raise "TableNameIsEmptyExeption: run insert_into(table_name) first"
		ex_str = "INSERT INTO " + self.__insert_into_tablename_ + " VALUES ("
		if type(var_tuple) is list:
			if len():
				tmp_var_tuple = var_tuple[0]
		else:
			tmp_var_tuple = var_tuple
		for i in tmp_var_tuple:
			if i != tmp_var_tuple[len(tmp_var_tuple) - 1]:
				ex_str += '?,'
			else:
				ex_str += '?'
		ex_str += ');'
		self.__db_.execute(ex_str, var_tuple)
		return self

	def select(self, table_name):
		"""equals to "SELECT * FROM table_name;
		Returns iterable cursor object, iteration object is tuple"""
		self.__select_query_ = "SELECT * FROM " + table_name
		return self

	def where(self, symbols_tuple):
		pass

	def order_by(self, what):
		pass

	def run(self):
		if self.__select_query_ != None:
			return self.__get_()
		elif self.__insert_into_tablename_ != None:
			return self.__commit_()


	def __init_db_(self):
		"""Open or create database with following path"""
		self.__db_ = sqlite3.connect(self.__path_)

	def __get_(self):
		tmp = self.__db_.execute(self.__select_query_ + ';')
		self.__select_query_ = None
		self.__cursor_ = tmp
		return self

	def fetch(self):
		tmp = self.__cursor_.fetchall()
		self.__cursor_ = None
		return tmp

	def fetchone(self):
		tmp = self.__cursor_.fetchone()
		self.__cursor_ = None
		return tmp

	def __commit_(self):
		self.__db_.commit()
		self.__insert_into_tablename_ = None

	def close_db(self):
		self.__db_.close()

	def get_path(self):
		return self.__path_

	def __get_db_instance_(self):
		return self.__db_


if __name__ == '__main__':
	print('Initializing database')
	if __name__ == '__main__' and __package__ is None:
		from os import sys, path
		sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
	from settings import DATABASE_PATH
	Database(DATABASE_PATH)
