from BinaryTree import BinarySearchTree


def make_tree(data):
    obj = BinarySearchTree(data[0])
    for i in range(1, len(data)):
        obj.insert(data[i])

    return obj


l = [5, 9, 1, 4, 6, 7, 0, -4]
ls = ["mango", "banana", "orange", "pineapple"]
obj1 = make_tree(l)
obj2 = make_tree(ls)

print(obj1.in_order_traversal())
print(obj1.pre_order_traversal())
print(obj1.post_order_traversal())

print(obj2.in_order_traversal())
print(obj2.min())
print(obj2.max())
print(obj2.pre_order_traversal())
print(obj2.post_order_traversal())

obj1.delete(5)
print(obj1.in_order_traversal())