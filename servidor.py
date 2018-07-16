from socket import *
import _thread
import sys
from ProtocoloCloud import *

def con_cliente(client_socket,addr, p):
	while True:
		msg = client_socket.recv(1024) 
		p.setMensagem(msg.decode())
		client_socket.send(p.retornaResposta().encode()) 
	client_socket.close()

if __name__ == "__main__":
	port = int(sys.argv[1])
	host = "::"

	service_socket = socket(AF_INET6, SOCK_STREAM)
	service_socket.bind((host, port))       
	service_socket.listen(100)               
	p = ProtocoloCloud()

	while True:
		client_socket, addr = service_socket.accept()     
		_thread.start_new_thread(con_cliente,(client_socket,addr,p))
	
	service_socket.close()