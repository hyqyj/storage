import socket
import sys
from threading import *
import ssl

def main():
	global size, xport, max_conn
	try:
		xport = int(input("Enter a listening port: *"))
	except KeyboardInterrupt:
		sys.exit(0)

	max_conn = 5
	size = 8192

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('',xport))
		s.listen(max_conn)
		print("[*] Intializing socket... Done.")
		print("[*] Scoket binded successfully...")
		print(f"[*] Server started successfully [{xport}]")
	except Exception as e:
		print(e)
		sys.exit(2)

	while True:
		try:
			conn, addr = s.accept()
			data = conn.recv(size)
			print(data)
			k = Thread(target=conn_string, args=(conn, data, addr))
			k.start()
		except KeyboardInterrupt:
			s.close()
			print("\n[*] Shutting dowm...")
			sys.exit(1)
	s.close()

def conn_string(conn, data, addr):
	try:
		data = str(data)
		first_line = data.split("\n")[0]
		url = first_line.split(" ")[1]

		http_pos = url.find("://")
		if http_pos == -1:
			temp = url
		else:
			temp = url[(http_pos + 3):]

		port_pos = temp.find(":")

		webserver_pos = temp.find("/")
		if webserver_pos == -1:
			webserver_pos = len(temp)
		webserver = ""
		port = -1

		if port_pos == -1 or webserver_pos < port_pos:
			port = 80
			webserver = temp[:webserver_pos]
		else:
			port = int(temp[(port_pos + 1):][:webserver_pos - port_pos - 1])
			webserver = temp[:port_pos]

		print(webserver)
		proxy_server(webserver, port, conn, data, addr)
	except Exception as e:
		print(e)
	
def proxy_server(webserver, port, conn, data, addr):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((webserver,port))
		s.send(bytes(data))

		while True:
			reply = s.recv(size)
			if len(reply) > 0:
				conn.send(bytes(reply))

				dar = float(len(reply))
				dar = float(dar / 1024)
				dar = "{}.3s".format(dar)
				print(f"[*] Request done: { addr[0] } => { dar } <= { webserver }")
			else:
				break

		s.close()
		conn.close()
	except Exception as e:
		s.close()
		conn.close()
		sys.exit(1)

if __name__ == '__main__':
	main()
