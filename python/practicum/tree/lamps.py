# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return find_max(root)


def find_max(n, max_v=0):
    if n.right is None and n.left is None:
        max_v = max(n.value, max_v)
    elif n.right is None and n.left is not None:
        max_v = find_max(n.left, max_v)
    elif n.right is not None and n.left is None:
        max_v = find_max(n.right, max_v)
    else:
        max_v = max(find_max(n.left, max_v), find_max(n.right, max_v), n.value)
    return max_v


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
