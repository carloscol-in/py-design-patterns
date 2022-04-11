class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(self.plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        processed_text = ''
        for l, c in zip (self.plain_text, self.caps):
            processed_text += l.upper() if c else l
        return processed_text

class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        t_range = self.TextRange(start, end)
        self.formatting.append(t_range)
        return t_range

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)
        return ''.join(result)

if __name__ == '__main__':
    ft = FormattedText('hello, world')
    ft.capitalize(0, 5)
    print(ft)

    btf = BetterFormattedText('hello, world!')
    btf.get_range(3, 8).capitalize = True
    print(btf)