class Node:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드 값

def inorder(root):
    """중위 순회 (Left -> Root -> Right)"""
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# 트리 생성
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

inorder(root)  # 4 2 1 3
