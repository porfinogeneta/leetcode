def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    idea: Mamy dwa wskaźniki, lewy i prawy, lewy przesuwamy dopóki nie natrafimy na 0,
    prawy dopóki jest za lewym albo nie natrafimy na liczbę różną od 0. Potem, jak znajdziemy
    odpowiednie liczby to po prostu je zamieniamy i dalej przesuwamy. Czas: O(n)
    """
    left, right = 0, 0
    while right < len(nums):
        if nums[left] != 0:
            left += 1
        if right <= left or nums[right] == 0:
            right += 1
        if left < len(nums) and right < len(nums):
            nums[left], nums[right] = nums[right], nums[left]
    return nums