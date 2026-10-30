#аналогично 4 задаче алгоритм
def removeDuplicates(arr):
    if len(arr) == 0:
        return 0
    slow = 0 #перезаписывает без дубликатов 
    fast = 1 #идет по изначальной строке с дубликатами
    while fast < len(arr):
        if arr[fast] != arr[slow]: #символ новый - его запишем следующим 
            slow += 1
            arr[slow] = arr[fast]
        fast += 1 #проверяем след
    return slow + 1 #возвращаем число эл в массиве без дубликатов 

def main():
    arr = [1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(arr)
    print(arr[:k])

if __name__ == "__main__":
    main()
