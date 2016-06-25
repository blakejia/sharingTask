import socket, threading, time, os, sys, json

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_path = sys.path[0]
_configPath = _path[0:-len(os.path.basename(_path))] + "config.json"

_config = {}
with open(_configPath, "r") as _file:
    _config = json.loads(_file.read())

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_socket.bind((_config.get("server"), _config.get("port")))

_socket.listen(5)
print("waiting for connection ...")

os.mkdir(sys.path[0] + "/_temp")
TaskList = ["ls", "ls", "ls"]

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    _taskOpr = sock.recv(1024).decode("utf-8")
    sock.send(b'Welcome!')
    if _taskOpr == "requestTask":
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
