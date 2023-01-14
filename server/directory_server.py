from nodes.directory import Directory
from server import root, app, goto_dir
from flask import Flask, request, jsonify, current_app
from functools import wraps

@app.route('/directory', method='GET')
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
    return jsonify(name = dir.name, path = path, children = dir.children)

@app.route('/directory', methods=['POST', 'PUT'])
def add_directory():
    body = request.json
    if not all(key in body for key in ('name', 'max_elems', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        Directory(body['name'], body['max_elems'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400

@app.route('/directory', method='DELETE')
def delete_directory():
    path = request.args.get('path')
    try:
        dir: Directory = goto_dir(path)
        if not type(dir) == Directory:
            raise ValueError()
        dir.delete()
    except ValueError:
        return 'Wrong Path', 400
    except:
        return 'Not found', 404

@app.route('/directory', methods=['UPDATE', 'PATCH', 'POST'])
def update_directory():
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
    return 200