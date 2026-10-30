class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode() #фиктивный первый изел - единственные затраты памяти (меняем указатели далее только)
    current = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val: #сравниваем - какой эл след
            current.next = list1
            list1 = list1.next #переход
        else:
            current.next = list2
            list2 = list2.next
        current = current.next 
    if list1 is not None: # закончился цикл - ищем почему и дозаписываем
        current.next = list1 
    else:
        current.next = list2
    return dummy.next

def main():
    list1 = ListNode(3, ListNode(6, ListNode(8)))
    list2 = ListNode(4, ListNode(7, ListNode(9, ListNode(11))))
    result = mergeTwoLists(list1, list2)
    current = result
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print("None")


if __name__ == "__main__":
    main()
