from nodes.buffer_file import BufferFile
from nodes.directory import Directory
from types import NoneType


class TestBufferFile:
    def test_init(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_maxsize = 2
        file1 = BufferFile(file1_name, file1_maxsize, directory)
        assert file1.name == file1_name
        assert file1.MAX_BUF_FILE_SIZE == file1_maxsize
        assert file1.parent_dir == directory
    def test_delete(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_maxsize = 2
        file1 = BufferFile(file1_name, file1_maxsize, directory)

        file1.delete()

        assert not directory.children.__contains__(file1)
    def test_move(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_maxsize = 2
        file1 = BufferFile(file1_name, file1_maxsize, directory)
        dir2_name = "child1"
        dir2_maxElems = 1
        dir2 = Directory(dir2_name, dir2_maxElems, directory)

        file1.move(dir2)

        assert not directory.children.__contains__(file1)
        assert dir2.children.__contains__(file1)
    def test_push(self):
        file1_name = "file"
        file1_maxsize = 1
        file1 = BufferFile(file1_name, file1_maxsize)
        file1.push("test")
        assert file1.content == ["test"]
        file1.push("test2")
        assert file1.content == ["test"]
    def test_pop(self):
        file1_name = "file"
        file1_maxsize = 2
        file1 = BufferFile(file1_name, file1_maxsize)
        file1.push("test")
        file1.push("test2")
        file1.pop()
        assert file1.content == ["test2"]
        file1.pop()
        assert file1.content == []
        file1.pop()
        assert file1.content == []
    def test_readfile(self):
        file1_name = "file"
        file1_info = "test"
        file1_maxsize = 2
        file1 = BufferFile(file1_name, file1_maxsize)
        file1.push("test")
        assert file1.readfile() == file1_info