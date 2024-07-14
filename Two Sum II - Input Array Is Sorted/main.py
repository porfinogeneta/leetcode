

def twoSum(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        # przesuwamy prawy wskaźnik dopóki liczby na końcu na pewno są większe od wyniku, który chcemy
        if nums[r] + nums[l] > target:
            r -= 1
        # przesuwamy w lewy wskaźnik jeśli nasza suma okazała się za mała
        elif nums[r] + nums[l] < target:
            l += 1
        else:
            return l + 1, r + 1

if __name__ == '__main__':
    print(twoSum([1,3,4,5,7,11], 9))

