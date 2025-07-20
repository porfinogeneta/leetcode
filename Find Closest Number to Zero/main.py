def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        closest_num = float("inf")

        for n in nums:
            if abs(n) < abs(closest_num):
                closest_num = n

            if abs(n) == abs(closest_num):
                if n > closest_num:
                    closest_num = n
        
        return closest_num