from nodes.directory import Directory


class BinaryFile:
    def __init__(self, name, parent_dir: Directory | None, info) -> None:
        pass

    def delete(self):
        pass

    def move(self, new_parent_dir: "Directory"):
        pass

    def readfile(self):
        pass
