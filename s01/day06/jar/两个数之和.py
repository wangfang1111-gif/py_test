#author:wang fang
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return print(i,j)
                """
        for i in range(1, len(nums)):
                    temp = nums[:i]
                    print(temp)
                    num1 = target - nums[i]
                    if num1 in temp:
                        j = temp.index(num1)
                        return print(i,j)
nums=[3,2,4, 7, 11, 15]
target=11
r1=Solution()
r1.twoSum(nums,target)
