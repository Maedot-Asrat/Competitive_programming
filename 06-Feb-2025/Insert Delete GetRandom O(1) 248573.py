# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.arr=[]
        self.position={}
    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arr.append(val)
            self.position[val] = len(self.arr) - 1
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.position:
            idx, last = self.position[val], self.arr[-1]
            self.arr[idx], self.position[last] = last, idx
            self.arr.pop(); self.position.pop(val, 0)
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()