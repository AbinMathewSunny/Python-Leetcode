class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        length2=length
        for i in range(length):
           if nums[i] ==val:
               nums[i] = -1
               length2-=1
        nums.sort(reverse=True)
        return length2    
       
        