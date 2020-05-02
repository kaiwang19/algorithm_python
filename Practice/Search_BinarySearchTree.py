def inoder_tree_walk(x):
    """
    A method to print all the elements in a binary search tree
    There are 3 ways to do this job: inorder/preorder/postorder -tree-walk
    Introduction to Algorithms (3rd Chinese Edition), page 162.
    Authored by Kai Wang.
    2020-04-25
    :param x: one element in BST
    :return:
    """
    if not x:  # if x is not None:
        inoder_tree_walk(x.left)
        print(x.key)
        inoder_tree_walk(x.right)


def tree_search(x, k):
    """
    Introduction to Algorithms (3rd Chinese Edition), page 163.
    Authored by Kai Wang.
    2020-04-25
    :param x: root node
    :param k: targeted value
    :return:
    """
    if (x is None) | (k == x.key):
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while (not x) & (k != x.key):
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while not x.left:
        x = x.left
    return x


def tree_maximum(x):
    while not x.right:
        x = x.right
    return x


def tree_successor(x):
    if not x.right:
        return tree_minimum(x.right)
    y = x.parent
    while (not y) & (x == y.right):
        x = y
        y = y.parent
    return y


def tree_insert(T, z):
    y = None
    x = T.root
    while not x:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if not y:
        T.root = x   # empty tree
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z



