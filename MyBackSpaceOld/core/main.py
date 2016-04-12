if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.router import Router
from http.server import HTTPServer
from app.app import init

import sys
from wsgiref.simple_server import make_server
if __name__ == "__main__":
	#server = make_server(sys.argv[1] if len(sys.argv) > 2 else '127.0.0.1', \
	#	int(sys.argv[2]) if len(sys.argv) > 2 else int(sys.argv[1]) if len(sys.argv) > 1 else 8080, Router)
	init()
	server = HTTPServer((sys.argv[1] if len(sys.argv) > 2 else '127.0.0.1', \
		int(sys.argv[2]) if len(sys.argv) > 2 else int(sys.argv[1]) if len(sys.argv) > 1 else 8080), Router)
	server.serve_forever()
