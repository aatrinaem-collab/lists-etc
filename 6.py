#За O(n) так как проходимся до половины строки 
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right: #сравниваем до середины строки
        if s[left] != s[right]: #просто сравниваем с двух концов
            return False #не совпали
        left += 1 #проверяем след пару элементов 
        right -= 1
    return True


def main():
    print(isPalindrome("radar"))
    print(isPalindrome("hello"))
    print(isPalindrome("abba"))


if __name__ == "__main__":
    main()
