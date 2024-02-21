def lengthOfLongestSubstring(s):
    letters = set() # set na literki
    res = 0
    l, r = 0, 0
    # idziemy po s i w razie powtórki skracamy prawą stronę window, usuwając prawy element z set
    while r < len(s):
        while s[r] in letters:
            letters.remove(s[l])
            l += 1
        letters.add(s[r])  # po usunięciu duplikatów dodajemy najbardziej prawy do listy
        res = max(res, r - l + 1) # odejmujemy indexy, czyli faktyczna długość będzie + 1
        r += 1
    return res

print(lengthOfLongestSubstring("abcabcbb"))