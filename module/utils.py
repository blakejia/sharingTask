DEFAULT_BUFF_LEN = 4

def recvData(sock, addr):
    _data = ""
    while True:
        _tempData = sock.recv(DEFAULT_BUFF_LEN).decode("utf-8")
        print(len(_tempData))
        if len(_tempData) == 0:
            break
        _data += _tempData

    return _data
