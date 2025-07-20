def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i, j = 0, 0

        while i < len(s):

            if j == len(t):
                return False

            if t[j] == s[i]:
                i += 1
            
            j += 1

        return True