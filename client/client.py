import socket, os, sys, json

_path = sys.path[0]
_configPath = _path[0:-len(os.path.basename(_path))] + "config.json"

_config = {}
with open(_configPath, "r") as _file:
    _config = json.loads(_file.read())

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.mkdir(sys.path[0] + "/_temp")

#print(_socket.recv(1024).decode('utf-8'))
#for data in [b'Michael', b'Tracy', b'Sarah']:
#    _socket.send(data)
#    print(_socket.recv(1024).decode('utf-8'))

while True:
    _socket.connect((_config.get("server"), _config.get("port")))
    _socket.send(b"requestTask")
    _task = json.loads(_socket.recv(1024).decode('utf-8'))
    _socket.send("")
    _socket.close()
    time.sleep(1)
