from server import root, app

@app.route('/directory', method='GET')
def get_directory():
    pass

@app.route('/directory', methods=['POST', 'PUT'])
def add_directory():
    pass

@app.route('/directory', method='DELETE')
def delete_directory():
    pass

@app.route('/directory', methods=['UPDATE', 'PATCH', 'POST'])
def update_directory():
    pass