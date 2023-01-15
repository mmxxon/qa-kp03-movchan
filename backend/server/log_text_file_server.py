from nodes.directory import Directory
from nodes.log_text_file import LogTextFile
from server.utils import goto_dir
from flask import request, jsonify, Blueprint

log_text_file_server = Blueprint('log_text_file_server', __name__)

@log_text_file_server.route('/log_text_file', methods=['GET'])
def get_log_text_file():
    path = request.args.get('path')
    try:
        file: LogTextFile = goto_dir(path)
        if not type(file) == LogTextFile:
            raise ValueError()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return jsonify(name = file.name, path = path, info = file.readfile())

@log_text_file_server.route('/log_text_file', methods=['POST', 'PUT'])
def add_log_text_file():
    body = request.json
    if not all(key in body for key in ('name', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        if len(list(filter(lambda a: a.name == body['name'], dir.children))) > 0:
            raise SystemError("Path was already taken")
        LogTextFile(body['name'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Created log file', 200

@log_text_file_server.route('/log_text_file', methods=['DELETE'])
def delete_log_text_file():
    path = request.args.get('path')
    try:
        file: Directory = goto_dir(path)
        if not type(file) == LogTextFile:
            raise ValueError()
        file.delete()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404
    return 'Deleted log file', 200

@log_text_file_server.route('/log_text_file', methods=['UPDATE'])
def move_log_text_file():
    path = request.args.get('path')
    new_path = request.args.get('new_path')
    try:
        file: LogTextFile = goto_dir(path)
        new_parent = goto_dir(new_path)
        if not (type(file) == LogTextFile and type(new_parent) == Directory):
            raise ValueError()
        file.move(new_parent)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Moved log file', 200

@log_text_file_server.route('/log_text_file', methods=['PATCH'])
def append_log_text_file():
    path = request.args.get('path')
    info = request.args.get('info')
    try:
        file: LogTextFile = goto_dir(path)
        if not type(file) == LogTextFile:
            raise ValueError()
        if not type(info) == str:
            raise SystemError("Info must be text")
        file.append(info)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 'Added info to log file', 200