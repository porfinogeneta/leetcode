# Boyer-Moore majority algorithm
def majorityElement(nums):
    counter = 0
    m = nums[0]
    for n in nums:
        if n == m:
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                counter = 1
                m = n
    return m