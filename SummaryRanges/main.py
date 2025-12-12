class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        res = []

        pos_idx = 0

        if len(nums) == 0:
            return []

        l, r = nums[pos_idx], nums[pos_idx]

    
        while pos_idx < len(nums):
            expected_next = nums[pos_idx] + 1
            pos_idx += 1


            if len(nums) == pos_idx:
                if r == l:
                    res.append(str(r))
                else:
                    elem = str(l) + "->" + str(r)
                    res.append(elem)
                break

            if nums[pos_idx] == expected_next:
                r += 1
            else:
                if r == l:
                    res.append(str(r))
                else:
                    elem = str(l) + "->" + str(r)
                    res.append(elem)

                l, r = nums[pos_idx], nums[pos_idx]
        
        return res
            