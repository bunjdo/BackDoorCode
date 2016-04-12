import os
from http.server import BaseHTTPRequestHandler
from mimetypes import guess_type
from urllib.parse import parse_qs
from cgi import parse_header, parse_multipart


class Router(BaseHTTPRequestHandler):
	routes_dict = {}

	@staticmethod
	def add_route(route, handler):
		Router.routes_dict[route] = handler

	@staticmethod
	def in_rotes(route):
		return route in Router.routes_dict

	def __prepare_url_(self, url):
		if '?' in url:
			split = url.split('?')
			path = split[0]
			params = parse_qs(split[1])
			return (path, params)
		else:
			return (url, {})

	def parse_POST(self):
		ctype, pdict = parse_header(self.headers['content-type'])
		if ctype == 'multipart/form-data':
			postvars = parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			postvars = parse_qs(
					str(self.rfile.read(length)), 
					keep_blank_values=1)
		else:
			postvars = {}
		return postvars

	def call(self, post={}):
		#if environ['PATH_INFO'] in self.routes_dict:
		#	start_response('200 OK', [('Content-Type', 'text/html')])
		#	return self.routes_dict[environ['PATH_INFO']]()
		#elif environ['PATH_INFO'].startswith('/assets/'):
		#	return [bytearray(open(os.path.dirname(os.path.realpath(__file__)) + '/..' + environ['PATH_INFO'], "rb").read())]
		#else:
		#	start_response('404 NotFound', [('Content-Type', 'text/html')])
		#	return self.routes_dict['404']()
		(path, params) = self.__prepare_url_(self.path)
		if path in Router.routes_dict:
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(Router.routes_dict[path]({ 'path': path, 'get': params, 'post': post }))

		elif path.startswith('/assets/'):
			filepath = os.path.dirname(os.path.realpath(__file__)) + '/..' + path.replace('../', '')
			mimetype = guess_type(filepath)[0]
			try:
				f = open(filepath, 'rb' ) 
				self.send_response(200)
				self.send_header('Content-type', 'application/octet-stream' if mimetype == None else mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			except:
				self.send_error(404,'File Not Found: %s' % self.path)
		else:
			self.send_error(404,'File Not Found: %s' % self.path)

	def do_GET(self):
		self.call()

	def do_POST(self):
		self.call(self.parse_POST())