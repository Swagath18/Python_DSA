from typing import List #It is often used in function signatures to indicate that a function should take an argument of a list type.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #saving the differnce value from target    
        diff_dict = {}

        for idx, num in enumerate(nums):
            diff = target - num

            #checking if the difference value present in saved value
            if diff in diff_dict:
                return [diff_dict[diff],idx] #returning index of saved diff and current index

            diff_dict[num]=idx #saving the diff to diff dictionary

        return None

problem = Solution()
nums = [2, 7, 3, 4]
target = 9
result = problem.twoSum(nums, target)
print(result)  # Output: [0, 1] (indices of numbers 2 and 7 that add up to 9)
