from nodes.binary_file import BinaryFile
from nodes.directory import Directory
from types import NoneType


class TestBinaryFile:
    def test_init(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_info = "test"
        file1 = BinaryFile(file1_name, file1_info, directory)
        assert file1.name == file1_name
        assert file1.info == file1_info
        assert file1.parent_dir == directory
    def test_delete(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_info = "test"
        file1 = BinaryFile(file1_name, file1_info, directory)

        file1.delete()

        assert not directory.children.__contains__(file1)
    def test_move(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_info = "test"
        file1 = BinaryFile(file1_name, file1_info, directory)
        dir2_name = "child1"
        dir2_maxElems = 1
        dir2 = Directory(dir2_name, dir2_maxElems, directory)

        file1.move(dir2)

        assert not directory.children.__contains__(file1)
        assert dir2.children.__contains__(file1)
    def test_readfile(self):
        file1_name = "file"
        file1_info = "test"
        file1 = BinaryFile(file1_name, file1_info)
        assert file1.readfile() == file1_info