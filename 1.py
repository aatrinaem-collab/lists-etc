# За О(н), так как каждый узел проходим один раз.
class ListNode: #односвязный список
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head): #как в лк. 
    prev = None
    current = head
    while current is not None: #проходимся по эл с первого
      # prev > current > next было
        nextNode = current.next
        current.next = prev 
      # current > prev поменяли указатель со след на предыдущий 
        prev = current # переходим к следующему узлу
        current = nextNode
    return prev


def main():
    head = ListNode(1, ListNode(2, ListNode(3)))
    result = reverseLinkedList(head)
    current = result
    while current is not None:
        print(current.val)
        current = current.next
    print("None")


if __name__ == "__main__":
    main()
