'''
из первой домашки
➔ Дан отсортированный по возрастанию массив целых чисел
и некоторое число target.
➔ Необходимо найти два числа в массиве, которые в сумме дают
заданное значение target, и вернуть их индексы.
'''
#один идет из начала, другой с конца. Если сумма маленька, то начальный увеличиваем, если большая, то конечный уменьшаем
#за О(н) так как i, j проходит не более н элементов
def two_sum(arr, target):
  i = 0
  j = len(arr) - 1
  while i<j:
    s = arr[j] + arr[i]
    if s == target:
      return [i, j]
    elif s<target:
      i+=1
    else:
      j-=1
  return []

if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9),   # -> [0, 1]
        ([1, 2, 3, 4], 100),   # -> []
    ]

    for arr, target in tests:
        result = two_sum(arr, target)
        if result:
            i, j = result
            print(f"arr={arr}, target={target} -> {result}, "
                  f"{arr[i]} + {arr[j]} = {arr[i] + arr[j]}")
        else:
            print(f"arr={arr}, target={target} -> пара не найдена")
