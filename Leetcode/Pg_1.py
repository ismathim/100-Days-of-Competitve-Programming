# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        len_=1
        if len(nums)==0:
            return 0
        else:
            for i in range (1, len(nums)):
                if nums[i]!=nums[i-1]:
                    nums[len_]=nums[i]
                    len_+=1
            return len_
