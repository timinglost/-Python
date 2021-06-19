class Errors(Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    __slots__ = ['root', 'left_child', 'right_child']

    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if new_node >= self.root:
                raise Errors('Некорректное значение')
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except Errors as p:
            print(p)

    def insert_right(self, new_node):
        try:
            if new_node <= self.root:
                raise Errors('Некорректное значение')
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except Errors as p:
            print(p)

    def get_right_child(self):
        try:
            if self.right_child is None:
                raise Errors('Правый потомок отсутствует')
            return self.right_child
        except Errors as p:
            print(p)
            print('Возвращаю корень')
            return self

    def get_left_child(self):
        try:
            if self.right_child is None:
                raise Errors('Левый потомок отсутствует')
            return self.left_child
        except Errors as p:
            print(p)
            print('Возвращаю корень')
            return self

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root

r = BinaryTree(8)
print('get_root_val ', r.get_root_val())
print('get_left_child() ', r.get_left_child())
r.insert_left(40)
print('get_left_child() ', r.get_left_child())
print('get_left_child().get_root_val() ', r.get_left_child().get_root_val())
r.insert_right(12)
print('get_right_child() ', r.get_right_child())
print('get_right_child().get_root_val() ', r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print('get_right_child().get_root_val() ', r.get_right_child().get_root_val())
