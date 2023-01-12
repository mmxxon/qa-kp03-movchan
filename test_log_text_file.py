from nodes.log_text_file import LogTextFile
from nodes.directory import Directory
from types import NoneType


class TestLogTextFile:
    def test_init(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1_info = "test"
        file1 = LogTextFile(file1_name, directory)
        assert file1.name == file1_name
        assert file1.parent_dir == directory
    def test_delete(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1 = LogTextFile(file1_name, directory)

        file1.delete()

        assert not directory.children.__contains__(file1)
    def test_move(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        file1_name = "file"
        file1 = LogTextFile(file1_name, directory)
        dir2_name = "child1"
        dir2_maxElems = 1
        dir2 = Directory(dir2_name, dir2_maxElems, directory)

        file1.move(dir2)

        assert not directory.children.__contains__(file1)
        assert dir2.children.__contains__(file1)
    def test_readfile(self):
        file1_name = "file"
        file1_info = "test"
        file1 = LogTextFile(file1_name)
        file1.append(file1_info)
        assert file1.readfile() == file1_info
        file1_info2 = "test2"
        file1.append(file1_info2)
        assert file1.readfile() == "testtest2"
     def test_append(self):
        file1_name = "file"
        file1_info = "test"
        file1 = LogTextFile(file1_name)
        file1.append(file1_info)
        assert file1.readfile() == file1_info
        file1_info2 = "test2"
        file1.append(file1_info2)
        assert file1.readfile() == "testtest2"