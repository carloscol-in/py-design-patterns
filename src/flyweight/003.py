class Sentence:
    def __init__(self, plain_text):
        # todo
        self.words = [self.Word(w) for w in plain_text.split(' ')]

    class Word:
        def __init__(self, text, capitalize: bool = False):
            self.text = text
            self.capitalize = capitalize
        
        def __str__(self):
            return self.text.upper() if self.capitalize else self.text

    def __getitem__(self, item):
        return self.words[item]

    def __str__(self):
        return ' '.join(str(word) for word in self.words)


if __name__ == '__main__':
    s = Sentence('hello world')
    s[1].capitalize = True
    print(s)