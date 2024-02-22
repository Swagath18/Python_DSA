#Two Sum III - Data sturcuture design # Linkedin #170
'''implement the TwoSum class:
1. TwoSum() initilize the TwoSum object, with an emoty array initially.
2. Void add(int number) Adds number to the data structure.
3. boolean find(int value) Return true if there exists any pair of numbers whose sum is equal to value, otherwsie, it returns false'''

##solution
class TwoSum:
  def __init__(self, arr):
    self.hashmap = {}
    self.arr = []
    self.n = 0

  def add(self, number: int)->None:
    self.hashmap[number]=self.n
    self.arr.append(number)
    self.n+=1

  def find(self, value:int)->bool:
    for i in range(self.n):
      curr = self.arr[i] #1,
      desired = value-curr #3=4-1,
      if desired in self.hashmap and self.hashmap[desired]!=i: 
        #print(self.hashmap)
        return True

    return False

#Input : ["TwoSum", "add", "add", "add", "find", "find"]
###
two_sum = TwoSum([])
two_sum.add(1)
two_sum.add(3)
two_sum.add(5)

print(two_sum.find(4))  # Returns True, as 1 + 3 = 4
print(two_sum.find(7))  # Returns False, as there are no two numbers that add up to 7
