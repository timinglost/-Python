from collections import Counter, deque


class HuffmanCoding:
    __slots__ = ['word', 'code_table', 'se']

    def __new__(cls, word):
        if type(word) != str:
            print('Введены некорректные данные')
            return None
        else:
            return super().__new__(cls)

    def __init__(self, word):
        self.word = word
        self.code_table = dict()
        letters = Counter(self.word)
        sorted_elements = deque(sorted(letters.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                for i, j in enumerate(sorted_elements):
                    if weight > j[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    sorted_elements.append((comb, weight))
        else:
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        self.se = sorted_elements[0][0]

    def watch(self):
        self.huffman_code(self.se)
        print(self.code_table)
        for i in self.word:
            print(self.code_table[i], end=' ')

    def huffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code(tree[0], path=f'{path}0')
            self.huffman_code(tree[1], path=f'{path}1')


a = HuffmanCoding('beep boop beer!')
a.watch()
