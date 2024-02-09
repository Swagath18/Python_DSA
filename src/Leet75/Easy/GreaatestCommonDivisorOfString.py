class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
    
        def GCD(a,b):
            while b:
                a, b = b, a%b 
            return a

        if str1 + str2 != str2 + str1:
            return ""

        greatest_length = GCD(len(str1), len(str2))

        largest_string = str1[:greatest_length]

        return largest_string

# Test cases
problem = Solution()
str1 = "ABAB"
str2 = "ABABAB"
output = problem.gcdOfStrings(str1, str2)
print(output)  # Expected Output: "AB"
