class Rna:
    def __init__(self, line):
        self.line = line
        self.itered = line

    def __str__(self):
        return self.line

    def __iter__(self):
        return iter(self.itered)

    def __hash__(self):
        return hash(self.line)

    def gc_content(self):
        self.count_gc = 0
        for el in self.line:
            if el == 'c' or el == 'g':
                self.count_gc += 1
            self.per_gc = self.count_gc / len(self.line) * 100
        return self.per_gc

    def reverse_complement(self):
        self.revers_ln = []
        for el in self.line:
            if el == 'a':
                self.revers_ln.append('u')
            if el == 'c':
                self.revers_ln.append('g')
            if el == 'u':
                self.revers_ln.append('a')
            if el == 'g':
                self.revers_ln.append('c')
        self.revers_line = ''.join(map(str, self.revers_ln))
        return self.revers_line

    def equal(self, other):
        self.other = other.line
        return self.line.__eq__(self.other)


class Dna(Rna):

    def reverse_complement(self):
        self.revers_ln = []
        for el in self.line:
            if el == 'a':
                self.revers_ln.append('t')
            if el == 'c':
                self.revers_ln.append('g')
            if el == 't':
                self.revers_ln.append('a')
            if el == 'g':
                self.revers_ln.append('c')
        self.revers_line = ''.join(map(str, self.revers_ln))
        return self.revers_line

    def transcribe(self):
        transcribed_ln = []
        for el in self.line:
            if el == 'a':
                transcribed_ln.append('u')
            if el == 'c':
                transcribed_ln.append('g')
            if el == 't':
                transcribed_ln.append('a')
            if el == 'g':
                transcribed_ln.append('c')
        transcribed_line = ''.join(map(str, transcribed_ln))
        transcribed_line = Rna(transcribed_line)
        return transcribed_line
