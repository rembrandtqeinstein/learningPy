import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
site = input('Enter the URL of the site to connect to: ')
host = site.split('/')

try:
    mysock.connect((host[2],80))
except:
    print('Not a valid URL, try http://, copy from the Browser')
    quit()

cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(site).encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()