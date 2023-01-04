from nodes.directory import Directory


class BufferFile:
    def __init__(self, name: str, maxSize, parent_dir: Directory | None = None):
        pass

    def delete(self):
        pass

    def move(self, new_parent_dir: "Directory"):
        pass

    def push(self, element):
        pass

    def pop(self):
        pass
