def removeDuplicates(nums):
    k = 1
    j = 1  # wskaźnik na to gdzie możemy wstawiać ewentualne duplikaty
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            k += 1
            j += 1
    print(nums)
    print(k)
    return k

nums = [1,1,2,2]
removeDuplicates(nums)