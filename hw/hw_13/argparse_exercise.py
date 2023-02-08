import argparse
import os


parser = argparse.ArgumentParser(description='Calculate the size of a directory or file in KB')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', help='Directory path')
group.add_argument('-f', '--file', help='File path')
parser.add_argument('-F', '--file-extension', help='File extension')
args = parser.parse_args()

def get_dir_size(dir_path, extension=None):
    size = 0
    for path, dirs, files in os.walk(dir_path):
        for f in files:
            if extension and not f.endswith(extension):
                continue
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return size / 1024

def get_file_size(file_path):
    return os.path.getsize(file_path) / 1024

if args.directory:
    dir_size = get_dir_size(args.directory, args.file_extension)
    print(f'The size of the directory "{args.directory}" is {dir_size} KB')

if args.file:
    file_size = get_file_size(args.file)
    print(f'The size of the file "{args.file}" is {file_size} KB')
