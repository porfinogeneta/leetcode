def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = ""

        i = 0

        while i < len(strs[0]):
            current_letter = strs[0][i]
            for w in strs:
                if i == len(w):
                    return prefix
                
                if w[i] != current_letter:
                    return prefix

            prefix += current_letter
            i += 1

        return prefix