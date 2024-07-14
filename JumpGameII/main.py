# rozwiązanie opiera się na tym, że nie interesuje nas na co skaczemy,
# tylko kiedy, skaczemy, a skaczemy tylko jak już dalej dojść nie można
# cały czas się przesuwamy i-tym indeksem i rozszerzamy zakres o maksymalny
# możliwy skok

def jump(nums):
    if len(nums) == 1:
        return 0
    endRange, maxReach, jumps = 0, 0, 0
    for i in range(len(nums)):
        maxReach = max(maxReach, nums[i] + i)
        if i == endRange:
            endRange = maxReach
            jumps += 1
        if endRange == len(nums) - 1:
            return jumps
    return jumps