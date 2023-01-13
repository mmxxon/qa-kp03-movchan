from server import root, app

@app.route('/binary_file', method='GET')
def get_binary_file():
    pass

@app.route('/binary_file', methods=['POST', 'PUT'])
def add_binary_file():
    pass

@app.route('/binary_file', method='DELETE')
def delete_binary_file():
    pass

@app.route('/binary_file', methods=['UPDATE', 'PATCH', 'POST'])
def update_binary_file():
    pass

