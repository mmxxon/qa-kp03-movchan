import requests


class TestServer:
    def test_get_dir(self):
        response = requests.get("http://localhost:3333/directory?path=/")
        assert response.json() == {"children": [], "name": "root", "path": "/"}

    def test_create_dir(self):
        response = requests.post(
            "http://localhost:3333/directory",
            json={"name": "dir2", "max_elems": 2, "path": "/"},
        )
        assert response.status_code == 200
        assert response.text == "Created directory"

    def test_delete_dir(self):
        response = requests.delete("http://localhost:3333/directory?path=/dir2")
        assert response.status_code == 200
        assert response.text == "Deleted directory"
        assert not requests.get("http://localhost:3333/directory?path=/dir2")

    def test_move_dir(self):
        requests.post(
            "http://localhost:3333/directory",
            json={"name": "dir1", "max_elems": 2, "path": "/"},
        )
        requests.post(
            "http://localhost:3333/directory",
            json={"name": "dir2", "max_elems": 2, "path": "/"},
        )
        response = requests.patch(
            "http://localhost:3333/directory?path=/dir1&new_path=/dir2"
        )
        assert response.status_code == 200
        assert response.text == "Moved directory"
        assert not requests.get("http://localhost:3333/directory?path=/dir1")
        assert requests.get("http://localhost:3333/directory?path=/dir2/dir1")

    def test_create_buffer_file(self):
        response = requests.post(
            "http://localhost:3333/buffer_file?path=/",
            json={"name": "buffer", "max_size": 2, "path": "/"},
        )
        assert response.status_code == 200
        assert response.text == "Created buffer file"

    def test_get_buffer_file(self):
        response = requests.get("http://localhost:3333/buffer_file?path=/buffer")
        assert response.status_code == 200
        assert response.json() == {"content": [], "name": "buffer", "path": "/buffer"}
        
    def test_push_to_buffer_file(self):
        response = requests.patch('http://localhost:3333/buffer_file?path=/buffer&action=push&element=elem')
        assert response.status_code == 200
        assert response.text == 'Pushed to file'
        response = requests.get("http://localhost:3333/buffer_file?path=/buffer")
        assert response.json() == {"content": ['elem'], "name": "buffer", "path": "/buffer"}
        
    def test_pop_from_buffer_file(self):
        response = requests.patch('http://localhost:3333/buffer_file?path=/buffer&action=pop')
        assert response.status_code == 200
        assert response.text == 'elem'
        response = requests.get("http://localhost:3333/buffer_file?path=/buffer")
        assert response.json() == {"content": [], "name": "buffer", "path": "/buffer"}
    
    def test_move_buffer_file(self):
        response = requests.request("UPDATE",
            "http://localhost:3333/buffer_file?path=/buffer&new_path=/dir2/dir1"
        )
        assert response.status_code == 200
        assert response.text == 'Moved buffer file'
        
    def test_delete_buffer_file(self):
        response = requests.delete("http://localhost:3333/buffer_file?path=/dir2/dir1/buffer")
        assert response.status_code == 200
        assert response.text == 'Deleted buffer file'
        assert not requests.get("http://localhost:3333/buffer_file?path=/dir2/dir1/buffer")
        
    def test_create_binary_file(self):
        response = requests.post(
            "http://localhost:3333/binary_file?path=/",
            json={"name": "binary", "info": "123", "path": "/"},
        )
        assert response.status_code == 200
        assert response.text == "Created binary file"

    def test_get_binary_file(self):
        response = requests.get("http://localhost:3333/binary_file?path=/binary")
        assert response.status_code == 200
        assert response.json() == {"name": "binary", "info": "123", "path": "/binary"}
    
    def test_move_binary_file(self):
        response = requests.request("UPDATE",
            "http://localhost:3333/binary_file?path=/binary&new_path=/dir2/dir1"
        )
        assert response.status_code == 200
        assert response.text == 'Moved binary file'
        
    def test_delete_binary_file(self):
        response = requests.delete("http://localhost:3333/binary_file?path=/dir2/dir1/binary")
        assert response.status_code == 200
        assert response.text == 'Deleted binary file'
        assert not requests.get("http://localhost:3333/binary_file?path=/dir2/dir1/binary")

    def test_create_log_text_file(self):
        response = requests.post(
            "http://localhost:3333/log_text_file?path=/",
            json={"name": "log_text_file", "path": "/"},
        )
        assert response.status_code == 200
        assert response.text == "Created log file"

    def test_get_log_text_file(self):
        response = requests.get("http://localhost:3333/log_text_file?path=/log_text_file")
        assert response.status_code == 200
        assert response.json() == {"name": "log_text_file", "path": "/log_text_file", "info": ""}
        
    def test_append_log_text_file(self):
        response = requests.patch(
            "http://localhost:3333/log_text_file?path=/log_text_file&info=test"
        )
        assert response.status_code == 200
        assert response.text == 'Added info to log file'
        response = requests.get("http://localhost:3333/log_text_file?path=/log_text_file")
        assert response.json() == {"name": "log_text_file", "path": "/log_text_file", "info": "test"}
            
    def test_move_log_text_file(self):
        response = requests.request("UPDATE",
            "http://localhost:3333/log_text_file?path=/log_text_file&new_path=/dir2/dir1"
        )
        assert response.status_code == 200
        assert response.text == 'Moved log file'

        
    def test_delete_log_text_file(self):
        response = requests.delete("http://localhost:3333/log_text_file?path=/dir2/dir1/log_text_file")
        assert response.status_code == 200
        assert response.text == 'Deleted log file'
        assert not requests.get("http://localhost:3333/log_text_file?path=/dir2/dir1/log_text_file")
