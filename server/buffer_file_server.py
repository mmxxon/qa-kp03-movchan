from nodes.buffer_file import BufferFile
from nodes.directory import Directory
from server import root, app, goto_dir
from flask import Flask, request, jsonify

@app.route('/buffer_file', method='GET')
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

@app.route('/buffer_file', methods=['POST', 'PUT'])
def add_buffer_file():
    body = request.json
    if not all(key in body for key in ('name', 'max_size', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        BufferFile(body['name'], body['max_size'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400

@app.route('/buffer_file', method='DELETE')
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

@app.route('/buffer_file', methods=['UPDATE'])
def update_buffer_file():
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
    return 200

@app.route('/buffer_file', methods=['PATCH'])
def modify_buffer_file():
    action = request.args.get('action')
    path = request.args.get('path')
    try:
        file: BufferFile = goto_dir(path)
        match action:
            case "push":
                push_to_file(request.args, file)
            case "pop":
                pop_from_file(request.args, file)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400
    return 200
    
def push_to_file(args, file):
    pass

def pop_from_file(args, file):
    pass