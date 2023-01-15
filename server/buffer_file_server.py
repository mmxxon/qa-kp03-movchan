from nodes.buffer_file import BufferFile
from nodes.directory import Directory
from server.utils import goto_dir
from flask import request, jsonify, Blueprint

buffer_file_server = Blueprint('buffer_file_server', __name__)

@buffer_file_server.route('/buffer_file', methods=['GET'])
def get_buffer_file():
    path = request.args.get('path')
    try:
        file: BufferFile = goto_dir(path)
        if not type(file) == BufferFile:
            raise ValueError()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return jsonify(name = file.name, path = path, content = file.readfile())

@buffer_file_server.route('/buffer_file', methods=['POST', 'PUT'])
def add_buffer_file():
    body = request.json
    if not all(key in body for key in ('name', 'max_size', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        if len(list(filter(lambda a: a.name == body['name'], dir.children))) > 0:
            raise SystemError("Path was already taken")
        BufferFile(body['name'], body['max_size'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Created buffer file', 200

@buffer_file_server.route('/buffer_file', methods=['DELETE'])
def delete_buffer_file():
    path = request.args.get('path')
    try:
        file: BufferFile = goto_dir(path)
        if not type(file) == BufferFile:
            raise ValueError()
        file.delete()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return 'Deleted buffer file', 200

@buffer_file_server.route('/buffer_file', methods=['UPDATE'])
def move_buffer_file():
    path = request.args.get('path')
    new_path = request.args.get('new_path')
    try:
        file: BufferFile = goto_dir(path)
        new_parent = goto_dir(new_path)
        if not (type(file) == BufferFile and type(new_parent) == Directory):
            raise ValueError()
        file.move(new_parent)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Moved buffer file', 200

@buffer_file_server.route('/buffer_file', methods=['PATCH'])
def modify_buffer_file():
    action = request.args.get('action')
    path = request.args.get('path')
    try:
        file: BufferFile = goto_dir(path)
        if not type(file) == BufferFile:
            raise ValueError()
        match action:
            case "push":
                push_to_file(request.args, file)
            case "pop":
                return pop_from_file(file), 200
            case _:
                raise SystemError("Wrong action")
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Pushed to file', 200
    
def push_to_file(args, file: BufferFile):
    element = request.args.get('element')
    if not element:
        raise SystemError("No element")
    file.push(element)

def pop_from_file(file: BufferFile):
    return file.pop()