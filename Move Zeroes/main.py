def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    first_zero_left = 0
    first_num_left = first_zero_left
    while first_num_left < len(nums):
        if nums[first_zero_left] != 0:
            first_zero_left += 1
        first_num_left = first_zero_left + 1
        if first_num_left >= len(nums):
            break
        if nums[first_num_left] == 0:
            first_num_left += 1
        if first_num_left >= len(nums):
            break
        nums[first_zero_left], nums[first_num_left] = nums[first_num_left], nums[first_zero_left]

    return nums

if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))
    print(moveZeroes([0,1]))
    print(moveZeroes([1]))