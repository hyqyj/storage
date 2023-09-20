import socket
import sys
import ssl
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except msg:
	print('failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1])
	sys.exit()
print("socket created!")

#host = 'www.oschina.net'
host = 'www.baidu.com'
port = 80
try:
	remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)
s.connect((remote_ip, port))
print("socket connect to " + host + ' on ip ' + remote_ip)
#message = b'CONNECT www.baidu.com:443 HTTP/1.0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n\r\n'
message = b'GET / HTTP/1.1\r\nHost: www.baidu.com:80\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79\r\n\r\n'
#message = b'CONNECT www.baidu.com:80 HTTP/1.1\r\nHost: www.baidu.com:80\r\nProxy-Connection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79\r\n\r\n'
try:
	s.send(message)
except OSError as f:
	print("send failed")
	sys.exit()

print("Message send successfully")
while True:
	if len(s.recv(1024)) > 0:

		print(s.recv(1024))
	else:
		pass
s.close()