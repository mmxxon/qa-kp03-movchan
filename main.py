from nodes.directory import Directory
from nodes.binary_file import BinaryFile
from nodes.log_text_file import LogTextFile
from nodes.buffer_file import BufferFile

root = Directory("root", 3)
dir1 = Directory("dir1", 3, root)
dir2 = Directory("dir2", 3, root)
dir3 = Directory("dir3", 3, root)
print()
