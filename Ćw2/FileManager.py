class FileManager:
    def __init__(self,name):
        self.name = name

    def read_file(self):
        with open(self.name, 'r', encoding='utf-8') as file_reader:
            for linia in file_reader:
                print(linia, end='')

    def update_file(self):
        with open(self.name, 'a', encoding='utf-8') as file_updater:
            file_updater.write("Sample")
