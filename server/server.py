import socket, threading, time, os, sys, json

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_path = sys.path[0]
_rootPath = _path[0:-len(os.path.basename(_path))]
_configPath = _rootPath + "config.json"

sys.path.append(_rootPath)
from module.utils import *

_config = {}
with open(_configPath, "r") as _file:
    _config = json.loads(_file.read())

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_socket.bind((_config.get("server"), _config.get("port")))

_socket.listen(5)

if not os.path.exists(sys.path[0] + "/_temp"):
    os.mkdir(sys.path[0] + "/_temp")

TaskList = ["ls", "ls", "ls"]
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    _taskOpr = recvData(sock, addr)
    if _taskOpr == "requestTask":
        print(len(TaskList))
        if len(TaskList) == 0:
            sock.close()
            return

        sock.sendall(TaskList.pop(0).encode("utf-8"))
        _result= sock.recv(DEFAULT_BUFF_LEN).decode("utf-8")
        sock.close()
    elif _taskOpr == "pushTask":
        data = sock.recv(DEFAULT_BUFF_LEN).decode("utf-8")
        TaskList.append(data)
        sock.close()

    print('Connection from %s:%s closed.\n' % addr)


while True:
    sock, addr = _socket.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
