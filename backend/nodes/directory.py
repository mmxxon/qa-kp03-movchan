class Directory:
    def __init__(
        self,
        name: str,
        dir_max_elems=0,
        parent_dir=None,
    ):
        self.name = name
        self.DIR_MAX_ELEMS = dir_max_elems
        self.parent_dir = parent_dir
        self.children = []
        if parent_dir is not None:
            if self.parent_dir.DIR_MAX_ELEMS > len(self.parent_dir.children):
                self.parent_dir.children.append(self)
                print("Created directory ", self.name, " under", self.parent_dir.name)
            else:
                raise SystemError(
                    "Directory ",
                    self.name,
                    " cannot be created under ",
                    self.parent_dir.name,
                    " due to exceeding DIR_MAX_ELEMS of ",
                    self.parent_dir.DIR_MAX_ELEMS,
                )
        else:
            print("Created directory ", self.name)

    def delete(self):
        print("Deleted directory ", self.name)
        if self.parent_dir != None:
            self.parent_dir.children.remove(self)
        for child in self.children:
            child.parent_dir = None

    def list_files(self):
        return self.children

    def move(self, new_parent_dir: "Directory"):
        if (len(new_parent_dir.children) == new_parent_dir.DIR_MAX_ELEMS):
            raise SystemError(
                "Directory ",
                self.name,
                " cannot be moved to ",
                new_parent_dir.name,
                " due to exceeding DIR_MAX_ELEMS of ",
                new_parent_dir.DIR_MAX_ELEMS,
            )
        print(
            "Moved directory ",
            self.name,
            " from ",
            self.parent_dir.name,
            " to ",
            new_parent_dir.name,
        )
        if self.parent_dir != None:
            self.parent_dir.children.remove(self)
        for child in self.children:
            child.parent_dir = None
        self.parent_dir = new_parent_dir
        new_parent_dir.children.append(self)
