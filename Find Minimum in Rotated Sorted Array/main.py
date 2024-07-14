def findMin(nums):
    l = 0
    r = len(nums) - 1
    res = nums[r]
    while l <= r:
        # jesteśmy w przedziale już posortowanym
        if nums[l] < nums[r]:
            res = min(res, nums[l])
        mid = (l+r) // 2
        # środek jest częścią rosnącej, większej części, zbadamy prawą część
        if nums[mid] >= nums[l]:
            l = mid + 1
            res = min(nums[mid], res)
        # środek jest częścią rosnącej mniejszej częsci, chcemy przeszukać jej lewą stronę
        else:
            res = min(nums[mid], res)
            r = mid - 1
    return res


nums = [11,13,15,17]
print(findMin(nums))