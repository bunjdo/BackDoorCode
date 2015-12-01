import re
from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATES_DIR

class Render:

	env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

	#@staticmethod
	#def get_env():
	#	if __env == None:
	#		return __env = Environment(loader=FileSystemLoader('templates'))
	#	return __env

	@staticmethod
	def render_template(template, data={}):
		""""""
		return str.encode(
			Render.env.get_template(template).render(data=data)
			)

	@staticmethod
	def render_string(_str):
		"""Renders string for returning from app function to server instead of using template for it.
		Strange..."""
		return str.encode(_str)


	@staticmethod
	def render_dict(dict):
		"""Renders string for returning from app function to server instead of using template for it.
		It is the same with json by the way..."""
		return str.encode(str(dict))

#	@staticmethod
#	def render_template(way_to_template, dict={}):
#		"""Renders template way_to_template for returning from app function to server.
#		Don't forget to create template also."""
#		template_file = open(way_to_template, 'r')
#		re.DOTALL
#		split_arr = re.split("(\\{%.*%\\})", template_file.read())
#		print(split_arr)
#		for el in split_arr:
#			if re.search('({[^}]+})', el):
#				pass
#		return [str.encode(template_file.read())]
