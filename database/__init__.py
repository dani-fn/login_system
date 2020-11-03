class User:

    def __init__(self):
        pass

    @staticmethod
    def file_exist(file):
        try:
            test = open(file, 'rt')
            test.close()
        except FileNotFoundError:
            return False
        else:
            return True

    @staticmethod
    def create_file(file):
        creating = open(file, 'wt+')
        creating.close()
        print(f'File {file} successfully created!')

    def read_file(self):
        pass

    def sign_up(self):
        pass
