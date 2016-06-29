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
    _taskOpr = recvData(sock)
    print(_taskOpr)
    if _taskOpr == "requestTask":
        if len(TaskList) == 0:
            sendData(sock, "")
            sock.close()
            print('Connection from %s:%s closed.\n' % addr)
            return

        _task = TaskList.pop(0)
        try:
            sendData(sock, _task)
            _result= recvData(sock)
        except:
            TaskList.append(_task)

        sock.close()
        print('Connection from %s:%s closed.\n' % addr)
    elif _taskOpr == "pushTask":
        data = sock.recv(DEFAULT_BUFF_LEN).decode("utf-8")
        TaskList.append(data)
        sock.close()
        print('Connection from %s:%s closed.\n' % addr)

while True:
    sock, addr = _socket.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
