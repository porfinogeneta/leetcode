def isPalindrome(s):
    # pierwsze wersja
    # st = "".join(l.lower() for l in s if l.isalnum())
    # return st[::] == st[::-1]
    # druga wersja, pointery
    left = 0
    right = len(s) - 1
    while (left < right):
        while left < right and not s[left].isalnum():
            left += 1
        while right > left and not s[right].isalnum():
            right -= 1
        if left <= right and s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome(" "))
    print(isPalindrome("race a car"))
    print(isPalindrome(",,,,,,,,,,,,acva"))
    print(isPalindrome(".,"))

