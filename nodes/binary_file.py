from nodes.directory import Directory


class BinaryFile:
    def __init__(self, name, parent_dir: Directory | None, info) -> None:
        self.name = name
        self.parent_dir = parent_dir
        self.info = info
        if parent_dir is not None:
            if self.parent_dir.DIR_MAX_ELEMS > len(self.parent_dir.children):
                self.parent_dir.children.append(self)
                print("Created binary file ", self.name, " under", self.parent_dir.name)
            else:
                print(
                    "Binary file ",
                    self.name,
                    " cannot be created under ",
                    self.parent_dir.name,
                    " due to exceeding DIR_MAX_ELEMS of ",
                    self.parent_dir.DIR_MAX_ELEMS,
                )
        else:
            print("Created binary file ", self.name)

    def delete(self):
        print("Deleted binary file ", self.name)
        if self.parent_dir != None:
            self.parent_dir.children.remove(self)

    def move(self, new_parent_dir: "Directory"):
        print(
            "Moved binary file ",
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

    def readfile(self):
        return self.info
