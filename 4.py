def isSubsequence(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b): #идем из начала каждой из строк
        if a[i] == b[j]: #если равны, то можно рассматривать (искать) след символ строки а 
            i += 1
        j += 1 #проверяем след эл строки б каждый шаг 
    return i == len(a) #если нашли все элементы первой строки, то победа


def main():
    print(isSubsequence("abc", "ahbgdc"))
    print(isSubsequence("abc", "acb"))


if __name__ == "__main__":
    main()
