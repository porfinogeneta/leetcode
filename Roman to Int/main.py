def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        roman_vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0

        while i < len(s):
            # substraction case
            if i + 1 < len(s) and roman_vals[s[i]] < roman_vals[s[i+1]]:
                res += (roman_vals[s[i+1]] - roman_vals[s[i]])
                i = i+1
            else:
                res += roman_vals[s[i]]
            i+=1

        return res