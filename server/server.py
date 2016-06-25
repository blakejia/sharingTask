import socket, threading, time

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_socket.bind(("127.0.0.1", 6008))

_socket.listen(5)
print("waiting for connection ...")

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    #sock.send(b'Welcome!')
    _taskOpr = sock.recv(1024).decode("utf-8")
    if cmp(_taskOpr, "requestTask"):
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = _socket.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
