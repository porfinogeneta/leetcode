
def three_sum(nums):
    nums.sort()
    triples = set()
    res = []
    for i in range(len(nums)):
        target = nums[i]
        # algorytm 2sum do sprawdzenie czy osiągniemy nasz target,
        # czyli naszpierwszy element z naszej trójki do sprawdzenia
        l = i+1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] + target == 0:
                triple = [target, nums[l], nums[r]]
                if tuple(triple) not in triples:
                    res.append(triple)
                    triples.add(tuple(triple))
                # żeby nie wpadać w wieczną pętlę przesuwamy wskaźnik
                l += 1
            # jeżeli suma jest większa od 0 mamy za duże liczby z prawej, zmniejszamy wskaźnik
            elif nums[l] + nums[r] + target > 0:
                r -= 1
            elif nums[l] + nums[r] + target < 0:
                l += 1

    return res

if __name__ == '__main__':
    print(three_sum([-2,0,1,1,2]))