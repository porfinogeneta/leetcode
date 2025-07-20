


def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    if arr[l] == target:
        return l
    return -1



print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))























# def search(nums, target):
#     def binRecu(l, r):
#         if l > r:
#             return -1
#         mid = (l+r) // 2
#         if nums[mid] < target:
#             return binRecu(mid + 1, r)
#         elif nums[mid] > target:
#             return binRecu(l, mid - 1)
#         elif nums[mid] == target:
#             return mid
#     return binRecu(0, len(nums) - 1)


# print(search([1,2,3,4,5,6,7,8,9], 3))