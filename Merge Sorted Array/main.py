def merge(nums1, m, nums2, n):
    # linear solution
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if nums1[i] > nums2[j] and i >= 0:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    # n^2 solution
    # for num in nums2:
    #     lst1 = m - 1  # ostatni element z dodawanego
    #     newidx = m  # index nowego elementu
    #     nums1[newidx] = num
    #     while lst1 >= 0 and nums1[lst1] > num:
    #         # jak element jest mniejszy to zamieniamy
    #         help = nums1[newidx]
    #         nums1[newidx] = nums1[lst1]
    #         nums1[lst1] = help
    #         lst1 -= 1
    #         newidx -= 1
    #     m += 1 # dodaliśmy jedną liczbę, więc idziemy dalej

    print(nums1)

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)