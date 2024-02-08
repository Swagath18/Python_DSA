class Solution:
    def romanToInt(self, s: str) -> int:

        romanInteger = {'I':1, 'V':5,'X':10,'L':50, 'C':100, 'D':500,'M':1000}

        result, previousValue = 0, 0

        last_idx = len(s)-1 #to iterate in reverse order

        for idx in range(last_idx,-1,-1):

            cur_value = romanInteger[s[idx]]
            #print(cur_value)

            if cur_value < previousValue: #checking I < V then it should be 4 ie IV
                result = result - cur_value
            else:
                result = result + cur_value # V>I then it should 6 ie VI

            previousValue = cur_value

        return result

problem = Solution()
roman_numeral = "MCMXCVI"
result = problem.romanToInt(roman_numeral)
print(result)  # Output: 9
