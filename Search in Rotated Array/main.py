def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target: return mid
        # jesteśmy w lewej, posortowanej części
        if nums[l] <= nums[mid]:
            # chcemy iść w prawo, jeśli target jest mniejszy od najmnijeszego w tej części
            # bo wtedy target musi być w prawym kawałku, albo chcemy iść w prawo
            # jak element jest po prostu większy od targeta, jak w standardowym binary search
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # jesteśmy w prawej, posortowanej części
        else:
            # chcemy iść w lewo, jeśli największy w tej posortowanej części, tj prawy jest mniejszy od target
            # to oznacza że wcześniej musiał być pivot, albo chcemy iść w lewo gdy po prostu
            # element mid jest mniejszy od targeta, jak w normalnym binary search'u
            if target > nums[r] or nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
    return -1

print(search([3,1], 1))