import hashlib

print('==================Задача-1==================')

string = input('Введите строку, состоящую только из маленьких латинских букв')

sum_substring = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) -1} различных подстрок в строке {string}')

print('==================Задача-2==================')

string = input("Введите строку из трех слов: ")
class Node:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
    def children(self):
        return self.left, self.right

def make_haffman_tree(node, code = ""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.children()
    result = {}
    result.update(make_haffman_tree(l, code + "0"))
    result.update(make_haffman_tree(r, code + "1"))
    return result

frequencies = {}
for char in string:
    if char not in frequencies:
        frequencies[char] = 0

    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse = True, key = lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

code_table = make_haffman_tree(tree[0][0])

coded = []
for char in string:
    coded.append(code_table[char])

print("Закодированная строка: %s" % "".join(coded))
