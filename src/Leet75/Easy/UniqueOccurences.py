#Unique number of Occurance #Apple
'''
given an array of integer arr, return true if the number of occurence of each value in the arry is unique or false otherwise
Input: [1,2,2,1,1,3] 
output: true 
explanation: no two values have same no of occurance

[-3,0,1,-3,1,1,1,-3,10,0] 
true

[1,2] 
false
'''

class Solution:
  def uniqueOccurences(self, arr:list):
    arr_count = {}
    for element in arr:
      if element in arr_count:
        arr_count[element]+=1
      else:
        arr_count[element]=1

    count, val = 0, 1
    for k,v in arr_count.items():
      if v == val:
        count+=1
      else:
        val = v

    if count>=2:
      return False
    else:
      return True

problem = Solution()
mylist = [1,2,3,1,1,2,2,3,3]
output = problem.uniqueOccurences(mylist)
print(output)
