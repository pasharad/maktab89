class FilteredEditor:
    Black_List1 = open("curse_words", "r")
    Black_List = Black_List1.readline().split(" ")

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.naughty = False

    def __enter__(self):
        self.file1 = open(self.filename, self.mode)
        self.file = self.file1.readline().split(" ")
        self.file_bad_words = []

        for i1 in FilteredEditor.Black_List:
            for j in self.file:
                if i1 == j:
                    self.file_bad_words.append(i1)
                    set(self.file_bad_words)

        if len(self.file_bad_words) != 0:
            self.naughty = True
            for i in self.file:
                if i in self.file_bad_words:
                    self.file = list(map(lambda x: x.replace(i, len(i)*"*"), self.file))

            self.file = " ".join(self.file)
            return f'edit : {self.file}'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file1.close()
        self.__class__.Black_List1.close()


with FilteredEditor("file1.txt", "r") as f:
    print(f)
