from flask import Flask
from nodes.binary_file import BinaryFile
from nodes.buffer_file import BufferFile
from nodes.directory import Directory
from nodes.log_text_file import LogTextFile

app = Flask(__name__)
root = Directory('root', 999)