# 단일 연결 리스트
class Node:
    """ 연결 리스트의 노드 정의 """
    def __init__(self, data):
        self.data = data  # 노드의 값
        self.next = None  # 다음 노드를 가리키는 포인터

class LinkedList:
    """ 단일 연결 리스트 (Singly Linked List) """
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드 (Head)

    def append(self, data):
        """ 연결 리스트의 끝에 새로운 노드 추가 """
        new_node = Node(data)
        if not self.head:  # 리스트가 비어있다면
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # 마지막 노드 찾기
            last_node = last_node.next
        last_node.next = new_node  # 마지막 노드의 next를 새 노드로 연결

    def delete(self, key):
        """ 특정 값을 가진 노드 삭제 """
        temp = self.head

        # 첫 번째 노드가 삭제할 노드인 경우
        if temp and temp.data == key:
            self.head = temp.next  # head를 다음 노드로 변경
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:  # 삭제할 노드가 없는 경우
            return

        prev.next = temp.next  # 이전 노드의 next를 삭제할 노드의 next로 변경
        temp = None  # 삭제

    def display(self):
        """ 연결 리스트의 모든 요소 출력 """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 사용 예시
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 1 -> 2 -> 3 -> None
ll.delete(2)
ll.display()  # 1 -> 3 -> None

# 이중 연결 리스트
class DNode:
    """ 이중 연결 리스트의 노드 정의 """
    def __init__(self, data):
        self.data = data
        self.prev = None  # 이전 노드 포인터
        self.next = None  # 다음 노드 포인터

class DoublyLinkedList:
    """ 이중 연결 리스트 (Doubly Linked List) """
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드

    def append(self, data):
        """ 연결 리스트 끝에 새로운 노드 추가 """
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node  # 이전 노드와 연결

    def delete(self, key):
        """ 특정 값을 가진 노드 삭제 """
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:  # 삭제할 노드가 없는 경우
            return

        if temp.prev:  # 이전 노드가 있으면 연결 변경
            temp.prev.next = temp.next
        if temp.next:  # 다음 노드가 있으면 연결 변경
            temp.next.prev = temp.prev

        if temp == self.head:  # 삭제할 노드가 head라면 변경
            self.head = temp.next

        temp = None  # 삭제

    def display(self):
        """ 연결 리스트의 모든 요소 출력 """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# 사용 예시
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # 1 <-> 2 <-> 3 <-> None
dll.delete(2)
dll.display()  # 1 <-> 3 <-> None
