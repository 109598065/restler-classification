import os

if __name__ == '__main__':
    path = 'grammar.py'
    backup_path = path.replace('.py', '_backup.py')

    if os.path.exists(path) and os.path.exists(backup_path):
        os.remove(path)
        os.rename(backup_path, path)
