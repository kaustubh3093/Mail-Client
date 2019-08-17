from socket import *
from base64 import *
from socket import *
import ssl

# Message to send
msg = '\r\nI love computer networks!'
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

# Port number may change according to the mail server
clientSocket.connect((mailserver, 587))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO gmail.com\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send STARTTLS command to encript socket with ssl.
strtlscmd = "STARTTLS\r\n"
clientSocket.send(strtlscmd)
recv2 = clientSocket.recv(1024)
print(recv2[:-2])
if recv[:3] != '220':
    print("Encyption failed.")

# Encrypt socket with ssl
sslClientSocket = ssl.wrap_socket(clientSocket)

#Check for authentication
username = b"**Enter Username**"
password = b"**Enter password**"
authorizationcmd = "AUTH LOGIN\r\n"

sslClientSocket.send(authorizationcmd)
recv2 = sslClientSocket.recv(1024)
print(recv2)
if recv2[:3] != '334':
    print("334 Not received from the server")

uname_encoded = b64encode(username)
pass_encoded = b64encode(password)

sslClientSocket.send(uname_encoded + b"\r\n")
recv3 = sslClientSocket.recv(1024)
print(recv3)
if recv3[:3] != '334':
    print("334 Not received from the server")

sslClientSocket.send(pass_encoded + b"\r\n")
recv4 = sslClientSocket.recv(1024)
print(recv4)
if recv4[:3] != '235':
    print("235 Not received from the server")
	
# Send MAIL FROM command and print server response.
mailfrom = "MAIL FROM: <**Enter mail from addr**>\r\n"
# Your code here
sslClientSocket.send(mailfrom)
recv5 = sslClientSocket.recv(1024)
print(recv5[:-2])
if recv5[:3] != '250':
    print('250 Not received from the server')


# Send RCPT TO command and print server response. 
rcptto = "RCPT TO: <**Enter mail to addr**>\r\n"
# Your code here
sslClientSocket.send(rcptto)
recv6 = sslClientSocket.recv(1024)
if recv6[:9] != "250 2.1.5":
    print('250 2.1.5 Not received from the server')

# Send DATA command and print server response. 
data = 'DATA\r\n'
# Your code here
sslClientSocket.send(data)
recv7 = sslClientSocket.recv(1024)
if recv7[:3] != '354':
    print('354 Not received from the server')

# Send message data.
# Your code here
print('Msg to send:')
print(msg)
sslClientSocket.send(msg)

# Message ends with a single period.
sslClientSocket.send(endmsg)
# Your code here
recv8 = sslClientSocket.recv(1024)
print(recv8[:-2])
if recv8[:9] != '250 2.0.0':
    print('250 2.0.0 Not received from the server')

# Send QUIT command and get server response.
quitcommand = 'QUIT\r\n'
# Your code here
sslClientSocket.send(quitcommand)
recv9 = sslClientSocket.recv(1024)
print(recv9[:-2])
if recv9[:9] != '221 2.0.0':
    print('221 2.0.0 Not received from the server')
sslClientSocket.close()
print('Program Successful')

