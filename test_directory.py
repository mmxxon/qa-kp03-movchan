from nodes.directory import Directory


class TestDirectory:
    def test_init(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        dir1_name = "child1"
        dir1_maxElems = 1
        dir1 = Directory(dir1_name, dir1_maxElems, directory)
        dir2_name = "child1"
        dir2_maxElems = 1
        dir2 = Directory(dir2_name, dir2_maxElems, directory)

        assert directory.name == name
        assert directory.DIR_MAX_ELEMS == maxElems
        assert directory.parent_dir == None
        assert dir1.parent_dir == directory
        assert directory.children.__contains__(dir1)
        assert not directory.children.__contains__(dir2)

    def test_delete(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        dir1_name = "child1"
        dir1_maxElems = 1
        dir1 = Directory(dir1_name, dir1_maxElems, directory)

        dir1.delete()

        assert not directory.children.__contains__(dir1)

    def test_list_files(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        dir1_name = "child1"
        dir1_maxElems = 1
        dir1 = Directory(dir1_name, dir1_maxElems, directory)

        files = directory.list_files()

        assert files == [dir1]

    def test_move(self):
        name = "parent"
        maxElems = 1
        directory = Directory(name, maxElems)
        dir1_name = "child1"
        dir1_maxElems = 1
        dir1 = Directory(dir1_name, dir1_maxElems, directory)
        dir2_name = "child1"
        dir2_maxElems = 1
        dir2 = Directory(dir2_name, dir2_maxElems, directory)

        dir1.move(dir2)

        assert not directory.children.__contains__(dir1)
        assert dir2.children.__contains__(dir1)
