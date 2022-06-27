import os

paths_correct = [
    'C:\\',
    'D:\\',
    'E:\\',
    '/home',
    '/home/bin'
]

paths_incorrect = [
    'D:/',
    '\\home',
    '\\home\\bin',
    'D:',
    'http://'
]


class FilePath:

    def get_path(self, number=20):
        paths = []
        root = "C:\\"
        for path, subdirs, files in os.walk(root, topdown=True):
            for name in files:
                if len(paths) > number:
                    return paths
                else:
                    paths.append(os.path.join(path, name))


file_path = FilePath()
file_paths = file_path.get_path(20)

paths = paths_correct + paths_incorrect + file_paths
