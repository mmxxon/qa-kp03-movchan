from nodes.directory import Directory
from nodes.log_text_file import LogTextFile
from server import root, app, goto_dir
from flask import Flask, request, jsonify

@app.route('/log_text_file', method='GET')
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
    return jsonify(name = file.name, path = path, content = file.readfile())

@app.route('/log_text_file', methods=['POST', 'PUT'])
def add_log_text_file():
    body = request.json
    if not all(key in body for key in ('name', 'path')):
        return 'Wrong request', 400
    try:
        dir: Directory = goto_dir(body['path'])
        if not type(dir) == Directory:
            raise ValueError()
        LogTextFile(body['name'], dir)
    except ValueError:
        return 'Wrong Path', 400
    except SystemError as error:
        return str(error), 400
    except:
        return 'Wrong Request', 400

@app.route('/log_text_file', method='DELETE')
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

@app.route('/log_text_file', methods=['UPDATE', 'PATCH', 'POST'])
def update_log_text_file():
    path = request.args.get('path')
    new_path = request.args.get('new_path')
    try:
        file: Directory = goto_dir(path)
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
    return 200