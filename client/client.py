import socket, os, sys, json, time

_path = sys.path[0]
_rootPath = _path[0:-len(os.path.basename(_path))]
_configPath = _rootPath + "config.json"

sys.path.append(_rootPath)
from module.utils import *

_config = {}
with open(_configPath, "r") as _file:
    _config = json.loads(_file.read())

if not os.path.exists(sys.path[0] + "/_temp"):
    os.mkdir(sys.path[0] + "/_temp")

while True:
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    DEFAULT_BUFF_LEN = _socket.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

    _connectResult = _socket.connect_ex((_config.get("server"), _config.get("port")))
    sendData(_socket, "requestTask")

    _taskJson = recvData(_socket)

    if _taskJson != "":
        sendData(_socket, "success")
        
    _socket.close()
    time.sleep(1)
