def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0

        l1 = len(word1)
        l2 = len(word2)

        res = ""

        while i < l1 and j < l2:
            if i == j:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            
        if i < l1:
            res += word1[i:]
        
        if j < l2:
            res += word2[j:]

        return res