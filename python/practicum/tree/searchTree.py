# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


#             19
#         /         \
#      11             31
#     /  \          /    \
#   3     15      25      43
#  /\     /\      /\      /\
# 2  8  13  18  22  28  37  55

def solution(root) -> bool:
    if root.left is None and root.right is None:
        return True
    res = True
    if root.left is not None:
        res = res and root.value > root.left.value and check(root.left, root.value, True) and solution(
            root.left)
    if root.right is not None:
        res = res and root.right.value > root.value and check(root.right, root.value, False) and solution(
            root.right)
    return res


def check(n, parent_value=None, is_left=True):
    if n.left is None and n.right is None or parent_value is None:
        return True
    if is_left:
        res = True
        res = res and n.value < parent_value
        if n.left is not None:
            res = res and n.value > n.left.value
        if n.right is not None:
            res = res and n.value < n.right.value < parent_value
        return res
    else:
        res = True
        res = res and n.value > parent_value
        if n.left is not None:
            res = res and n.value > n.left.value > parent_value
        if n.right is not None:
            res = res and n.value < n.right.value
        return res


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
