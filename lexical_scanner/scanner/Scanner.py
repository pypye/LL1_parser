class Scanner():
    def __init__(self, path):
        self.file_char = open(path, 'r', encoding='utf-8').read()
        self.count_char = 0
        self.count_line = 1
        self.count_col = 1
        self.remove_comment()

    def peek_word(self):
        self.remove_comment()
        word = ""
        count_char = self.count_char

        while count_char < len(self.file_char):
            char = self.file_char[count_char]
            if not char.isalpha(): break
            count_char += 1
            word += char
        
        return word
    
    def seek_word(self):
        while self.count_char < len(self.file_char):
            char = self.file_char[self.count_char]
            if not char.isalpha(): 
                break
            self.count_char += 1
            self.count_col += 1
        return self.count_char < len(self.file_char)
    
    
    def peek_char(self, n=1):
        self.remove_comment()
        char = self.file_char[self.count_char:self.count_char+n]
        return char        

    def seek_char(self, n=1):
        for i in range(self.count_char, min(self.count_char+n, len(self.file_char))):
            if self.file_char[i] == '\n':
                self.count_line += 1
                self.count_col = 0
            self.count_char += 1
            self.count_col += 1
        return self.count_char < len(self.file_char)
    

    def remove_comment(self):
        if self.file_char[self.count_char:self.count_char+2] == '//':
            while self.count_char < len(self.file_char) and self.file_char[self.count_char] != '\n':
                self.count_char += 1
                self.count_col += 1
            self.count_line += 1
            self.count_char += 1
            self.count_col = 1

        elif self.file_char[self.count_char:self.count_char+2] == '/*':
            while self.count_char+1 < len(self.file_char) and self.file_char[self.count_char:self.count_char+2] != '*/':
                if self.file_char[self.count_char] == '\n':
                    self.count_line += 1
                    self.count_col = 0
                self.count_char += 1
                self.count_col += 1
            self.count_char += 2
            self.count_col += 2
        
