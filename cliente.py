from socket import *
import sys
from ProtocoloCloud import *

def tipo_ip (ip_recv, flag) :
	ip = ''
	for res2 in sa :
		conteudo = str(sa)
		for res3 in conteudo :
			if (res3 == "'") : flag +=1
			if(flag == 1 and res3 != "'") : ip = ip+res3
	return ip

if __name__ == "__main__":
	server_name = sys.argv[1]
	server_port = int(sys.argv[2])
	client_socket = socket(AF_INET6, SOCK_STREAM)
	ipv4 = ''
	ipv6 = ''

	#saber o endereco correto, sem ser nome
	for res in (getaddrinfo(server_name, server_port, 0,SOCK_STREAM)) :
		flag = 0
		arq_ip, socktype, proto, canonname, sa = res
		sarq_ip = str(arq_ip)
		if(sarq_ip.find("AF_INET6") >= 0) : ipv6 = tipo_ip (sa, flag)
		elif (sarq_ip.find("AF_INET6") < 0): ipv4 = tipo_ip (sa, flag)
		else : print("erro")
	if(ipv6 == '') : server_name ='::FFFF:' + ipv4
	else : server_name = ipv6
	
	#cria a conexao
	client_socket.connect((server_name, server_port))
	
	while True :
		msg = input()
		client_socket.send(msg.encode())
		rcv_msg = client_socket.recv(1024)
		rcv_msg = rcv_msg.decode()
		print (rcv_msg)
		
	print("Conexao encerrada")
	client_socket.close()


	
