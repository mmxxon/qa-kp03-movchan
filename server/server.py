from types import NoneType
from flask import Flask
from nodes.binary_file import BinaryFile
from nodes.buffer_file import BufferFile
from nodes.directory import Directory
from nodes.log_text_file import LogTextFile

app = Flask(__name__)
root = Directory('root', 999)

def goto_dir(path):
    path = path.split('/')
    key = root
    for route in path:
        key = next(filter(lambda a: a.name == route, key.children), None)
        if type(key) == NoneType:
            return KeyError
    return key