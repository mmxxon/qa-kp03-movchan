import logging
from types import NoneType
from flask import Flask
from nodes.binary_file import BinaryFile
from nodes.buffer_file import BufferFile
from nodes.directory import Directory
from nodes.log_text_file import LogTextFile
from server.binary_file_server import binary_file_server
from server.buffer_file_server import buffer_file_server
from server.directory_server import directory_server
from server.log_text_file_server import log_text_file_server
from server.utils import root

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.register_blueprint(binary_file_server)
app.register_blueprint(buffer_file_server)
app.register_blueprint(directory_server)
app.register_blueprint(log_text_file_server)


@app.route("/reload", methods=["POST"])
def reload():
    root.children = []
    return 'Reloaded', 200
    

if __name__ == '__main__':
    app.run(port=3333, debug=True)