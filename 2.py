# быстрый двигается в 2 раза быстрее -> проходит в 2 раза больше. когда пройдет все, медленный указатель пройдет половину
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = middleNode(head)
    print(result.val)

if __name__ == "__main__":
    main()
