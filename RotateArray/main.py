def rotate(nums, k):
    # mądrzejszym podejściem jest odwrócenie obu części tablicy,
    # tej przechodzącej na prawo i tej na początku
    # po odwróceniu połówek uzyskamy taką kolejność że po odwróceniu całej tablicy
    # będziemy mieli przesunięcie, oprócz tego robimy modulo len(nums), bo to jest maksymalne
    # przesunięcie, potem się powtarza

    # dzielimy listę na dwie części, lewą (przechodzi w prawo) i prawą (przechodzi w lewo, na początek tablicy)
    # odwracamy P1, P2 a potem całość
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    k %= len(nums)
    # odwracamy prawą
    reverse(len(nums) - k, len(nums) - 1)
    # odwracamy lewą
    reverse(0, len(nums) - k - 1)
    # odwracamy całość
    reverse(0, len(nums) - 1)

    # rozwiązanie O(n^2)
    # t = 0
    # while k != t:
    #     t += 1
    #     v = nums[-1]
    #     for i in range(len(nums) - 2, -1, -1):
    #         nums[i + 1] = nums[i]
    #     nums[0] = v
    #
    return nums

print(rotate([1,2,3,4,5,6,7], 3))