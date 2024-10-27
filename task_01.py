class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end=" -> ")
            else:
                print(current.data, end="")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    @staticmethod
    def _get_middle(head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self

        middle = self._get_middle(self.head)
        next_to_middle = middle.next

        middle.next = None

        left = LinkedList()
        left.head = self.head

        right = LinkedList()
        right.head = next_to_middle

        left = left.merge_sort()
        right = right.merge_sort()

        sorted_list = LinkedList()
        sorted_list.head = self._sorted_merge(left.head, right.head)

        self.head = sorted_list.head
        return self

    def _sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)

        return result

    def merge_with(self, other_list):
        merged_list = LinkedList()
        merged_list.head = self._sorted_merge(self.head, other_list.head)
        return merged_list


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    print("Original list 1:")
    list1.print_list()
    list1.reverse()
    print("Reversed list 1:")
    list1.print_list()

    list3 = LinkedList()
    list3.append(3)
    list3.append(1)
    list3.append(2)
    list3.append(5)
    list3.append(4)

    print("Unsorted list 3:")
    list3.print_list()
    list3.merge_sort()
    print("Sorted list 3:")
    list3.print_list()

    print("List 1:")
    list1.print_list()
    print("List 2:")
    list2.print_list()

    merged_list = list1.merge_with(list2)
    print("Merged sorted list:")
    merged_list.print_list()
