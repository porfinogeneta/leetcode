def longestCommonPrefix(array1, array2):
    l1 = [str(elem) for elem in array1]
    l2 = [str(elem) for elem in array2]
    res = 0
    for n1,n2 in zip(l1,l2):
        lcp = 0
        for i in range(min(len(n1), len(n2))):
            if n1[i] == n2[i]:
                lcp += 1
            else:
                break
        res = max(res, lcp)
    return res

print(longestCommonPrefix([25,288,2655,54546,54,555], [2,255,266,244,26,5,544547]))