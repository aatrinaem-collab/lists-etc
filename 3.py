class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode() #фиктивная переменная - защита от удаления первой вершины
    dummy.next = head
    prev = dummy
    cur = head #она становится уже не первой и удаляется как другие из середины списка 
    while cur is not None:
        if cur.val == val: #совпало ->удаляем (меняем указатель у предыдущего элемента, пропуская текущий - удаленный )
            prev.next = cur.next
        else:
            prev = cur #к след шагу
        cur = cur.next
    return dummy.next #пропускаем фиктивную, возвращаем все после 


def main():
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(6))))) #12636
    result = removeElements(head, 6)
    cur = result
    while cur is not None:
        print(cur.val)
        cur = cur.next
    print("None")


if __name__ == "__main__":
    main()
