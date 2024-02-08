class Solution:
    def isPalindrome(self, x: int) -> bool:

        x_str = str(x) #converting integer to string format

        return x_str==x_str[::-1] #returning by checking the reverse of string

problem = Solution()
num = 1221
result = problem.isPalindrome(num)
print(result)