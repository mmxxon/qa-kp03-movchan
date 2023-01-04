from nodes.directory import Directory


class LogTextFile:
    def __init__(self, name, parent_dir: Directory | None) -> None:
        pass

    def delete(self):
        pass

    def move(self, new_parent_dir: "Directory"):
        pass

    def readfile(self):
        pass

    def append(self, content):
        pass
