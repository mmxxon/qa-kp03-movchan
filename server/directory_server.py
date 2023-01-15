from nodes.directory import Directory
from flask import current_app
from server.utils import goto_dir, root
from flask import request, jsonify, Blueprint

directory_server = Blueprint('directory_server', __name__)

@directory_server.route('/directory', methods=['GET'])
def get_directory():
    path = request.args.get('path')
    try:
        dir: Directory = goto_dir(path)
        if not type(dir) == Directory:
            raise ValueError()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return jsonify(name = dir.name, path = path, children = [{"name": key.name, "type": str(type(key).__name__).lower()} for key in dir.children])

@directory_server.route('/directory', methods=['POST', 'PUT'])
def add_directory():
    body = request.json
    if not all(key in body for key in ('name', 'max_elems', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        if len(list(filter(lambda a: a.name == body['name'], dir.children))) > 0:
            raise SystemError("Path was already taken")
        Directory(body['name'], body['max_elems'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Created directory', 200

@directory_server.route('/directory', methods=['DELETE'])
def delete_directory():
    path = request.args.get('path')
    try:
        dir: Directory = goto_dir(path)
        if not type(dir) == Directory:
            raise ValueError()
        if dir == root:
            raise SystemError("Cannot delete root")
        dir.delete()
    except SystemError as error:
        return str(error), 400
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return 'Deleted directory', 200

@directory_server.route('/directory', methods=['UPDATE', 'PATCH'])
def move_directory():
    path = request.args.get('path')
    new_path = request.args.get('new_path')
    try:
        dir: Directory = goto_dir(path)
        new_parent = goto_dir(new_path)
        if not (type(dir) == Directory and type(new_parent) == Directory):
            raise ValueError()
        dir.move(new_parent)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Moved directory', 200
