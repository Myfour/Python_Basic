from os.path import join


class FileObject:
    def __init__(self, filepath='.', filename='sample.txt'):
        print('init go --------------')
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        print('del go-----------')
        del self.file


if __name__ == '__main__':
    fileobj = FileObject()