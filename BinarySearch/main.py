def search(nums, target):
    def binRecu(l, r):
        if l > r:
            return -1
        mid = (l+r) // 2
        if nums[mid] < target:
            return binRecu(mid + 1, r)
        elif nums[mid] > target:
            return binRecu(l, mid - 1)
        elif nums[mid] == target:
            return mid
    return binRecu(0, len(nums) - 1)


print(search([1,2,3,4,5,6,7,8,9], 3))