# -*- coding: utf-8 -*-
import socket,threading

class ClientThread(threading.Thread):

	def __init__(self, conn, addr):
		self.conn = conn
		self.addr = addr
		threading.Thread.__init__(self)

	def run(self):
		self.conn.send("""Welcome to our calculating challenge.\n
			We believe that a true IT specialist should 
			be able to select and process any information obtained via scripts-software tricks.\n
			You can get a lot of points, if you calculate all that will offer by server.\n
			Do you ready to real great processing data?\n""")
		self.conn.send("Actions available: \n")
		self.conn.send("\t0 - Exit.\n")
		self.conn.send("\t1 - Go.\n")
		while True:
			try:
				data = self.conn.recv(1024)
				if data == "0\n":
					self.conn.send("Bye\n")
					self.disconnect()
					break
				elif data == "1\n":
					self.conn.send("Flag is DvCTF{tRiVi@_c0NN3cT1ioN}\n")
				else:
					self.conn.send("No options detected.\n")
			except socket.error, msg:
				print "Error! Addr: %s. Message: %s" % (self.addr, msg)
				self.disconnect()
				break

	def disconnect(self):
		print 'disconnected:', self.addr
		self.conn.close()		

if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('', 1337))
	sock.listen(2)
	while True:
		conn, addr = sock.accept()
		print 'connected:', addr
		ClientThread(conn,addr).start()
	sock.close()