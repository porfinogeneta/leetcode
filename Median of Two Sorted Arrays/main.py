def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    # A to ta krótsza tablica
    if len(A) > len(B):
        A, B = B, A

    total = len(A) + len(B)

    an = len(A)
    bn = len(B)

    low, high = 0, an
    left = (an + bn + 1) // 2  # left to środek, przesunięty na prawo, liczba elementów z większej tablicy

    while low <= high:

        # konstruujemy lewy podział
        midA = (low + high) // 2
        midB = left - midA  # midB to to co zostało z górnej tablicy

        lA = float("-inf")
        rA = float("inf")
        lB = float("-inf")
        rB = float("inf")

        if midA < an:
            rA = A[midA]
        if midB < bn:
            rB = B[midB]
        if midA - 1 >= 0:
            lA = A[midA - 1]
        if midB - 1 >= 0:
            lB = B[midB - 1]

        if lA <= rB and lB <= rA:
            if total % 2 == 1:
                return max(lA, lB)
            else:
                return ((max(lA, lB) + min(rA, rB)) / 2.0)
        elif lA > rB:
            high = midA - 1
        else:
            low = midA + 1



# print(findMedianSortedArrays([1,2,3,4], [1,2,3,4,5,6,7,8]))
print(findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10], [2]))