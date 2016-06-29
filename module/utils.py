DEFAULT_BUFF_LEN = 1024

def recvData(sock):
    _data = ""
    _lenght = int(sock.recv(DEFAULT_BUFF_LEN).decode("utf-8"))
    sock.send(b"head")
    while _lenght > 0:
        _recvLen = min(_lenght, DEFAULT_BUFF_LEN)
        _lenght = _lenght - _recvLen
        _tempData = sock.recv(_recvLen).decode("utf-8")
        _data += _tempData

    return _data

def sendData(sock, data):
    _data = str(data).encode("utf-8")
    sock.send(str(len(_data)).encode("utf-8"))
    _result = sock.recv(DEFAULT_BUFF_LEN).decode("utf-8")
    if _result != "head":
        return
    sock.sendall(_data)
