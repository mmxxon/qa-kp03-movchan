from flask import current_app
from types import NoneType
from nodes.directory import Directory

root = Directory('root', 999)

def goto_dir(path):
    path = list(filter(None, path.split('/')))
    key = root
    if len(path) == 0: return key
    for route in path:
        current_app.logger.info(path)
        temp = list(filter(lambda a: a.name == route, key.children))
        if len(temp) == 0:
            return ValueError
        key = temp[0]
    return key

