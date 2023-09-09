import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.56.101', 999)
message = b'This is our message. It will be sent all at once'

print('sending {!r}'.format(message))
sent = sock.sendto(message, server_address)

print('waiting to receive')
data, server = sock.recvfrom(4096)
print('received {!r}'.format(data))
