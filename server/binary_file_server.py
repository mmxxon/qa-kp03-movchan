from nodes.binary_file import BinaryFile
from nodes.directory import Directory
from server.utils import goto_dir
from flask import request, jsonify, Blueprint

binary_file_server = Blueprint('binary_file_server', __name__)

@binary_file_server.route('/binary_file', methods=['GET'])
def get_binary_file():
    path = request.args.get('path')
    try:
        file: BinaryFile = goto_dir(path)
        if not type(file) == BinaryFile:
            raise ValueError()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return jsonify(name = file.name, path = path, content = file.readfile())

@binary_file_server.route('/binary_file', methods=['POST', 'PUT'])
def add_binary_file():
    body = request.json
    if not all(key in body for key in ('name', 'info', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        if len(list(filter(lambda a: a.name == body['name'], dir.children))) > 0:
            raise SystemError("Path was already taken")
        BinaryFile(body['name'], body['info'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Created binary file', 200

@binary_file_server.route('/binary_file', methods=['DELETE'])
def delete_binary_file():
    path = request.args.get('path')
    try:
        file: Directory = goto_dir(path)
        if not type(file) == BinaryFile:
            raise ValueError()
        file.delete()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return 'Deleted binary file', 200

@binary_file_server.route('/binary_file', methods=['UPDATE', 'PATCH'])
def move_binary_file():
    path = request.args.get('path')
    new_path = request.args.get('new_path')
    try:
        file: Directory = goto_dir(path)
        new_parent = goto_dir(new_path)
        if not (type(file) == BinaryFile and type(new_parent) == Directory):
            raise ValueError()
        file.move(new_parent)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Moved binary file', 200
