from nodes.binary_file import BinaryFile
from nodes.directory import Directory
from server import root, app, goto_dir
from flask import Flask, request, jsonify

@app.route('/binary_file', method='GET')
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

@app.route('/binary_file', methods=['POST', 'PUT'])
def add_binary_file():
    body = request.json
    if not all(key in body for key in ('name', 'info', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        BinaryFile(body['name'], body['info'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400

@app.route('/binary_file', method='DELETE')
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

@app.route('/binary_file', methods=['UPDATE', 'PATCH', 'POST'])
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
    return 200
