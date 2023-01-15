from nodes.directory import Directory


class BufferFile:
    def __init__(self, name: str, max_size, parent_dir: Directory | None = None):
        self.name = name
        self.MAX_BUF_FILE_SIZE = max_size
        self.parent_dir = parent_dir
        self.content = []
        if parent_dir is not None:
            if self.parent_dir.DIR_MAX_ELEMS > len(self.parent_dir.children):
                self.parent_dir.children.append(self)
                print("Created buffer file ", self.name, " under", self.parent_dir.name)
            else:
                raise SystemError(
                    "Buffer file ",
                    self.name,
                    " cannot be created under ",
                    self.parent_dir.name,
                    " due to exceeding DIR_MAX_ELEMS of ",
                    self.parent_dir.DIR_MAX_ELEMS,
                )
        else:
            print("Created buffer file ", self.name)

    def delete(self):
        print("Deleted buffer file ", self.name)
        if self.parent_dir != None:
            self.parent_dir.children.remove(self)

    def move(self, new_parent_dir: "Directory"):
        if (len(new_parent_dir.children) == new_parent_dir.DIR_MAX_ELEMS):
            raise SystemError(
                "BufferFile ",
                self.name,
                " cannot be moved to ",
                new_parent_dir.name,
                " due to exceeding DIR_MAX_ELEMS of ",
                new_parent_dir.DIR_MAX_ELEMS,
            )
        print(
            "Moved buffer file ",
            self.name,
            " from ",
            self.parent_dir.name,
            " to ",
            new_parent_dir.name,
        )
        if self.parent_dir != None:
            self.parent_dir.children.remove(self)
        self.parent_dir = new_parent_dir
        new_parent_dir.children.append(self)

    def push(self, element):
        if self.MAX_BUF_FILE_SIZE == len(self.content):
            raise SystemError(
                "Buffer file ",
                self.name,
                " cannot be extended due to exceeding MAX_BUF_FILE_SIZE of ",
                self.MAX_BUF_FILE_SIZE,
            )
        else:
            self.content.append(element)

    def pop(self):
        if len(self.content) == 0:
            raise SystemError("Cannot pop element due to zero length")
        else:
            element = self.content[0]
            self.content.pop(0)
            return element

    def readfile(self):
        return self.content