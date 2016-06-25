import os

class Task:
    def __init__(self):
        self.fileList = []
        self.cmd = ""
        self.outputFile = {}

    def __del__(self):
        for _file in self.fileList:
            os.remove(_file)

