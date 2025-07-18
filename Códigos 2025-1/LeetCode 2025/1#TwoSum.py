#12/07/2025
#https://leetcode.com/problems/two-sum/description/
#this is the optimized code for concluding the first exercise(i think) of leetcode, theres another way that uses
#brute force i may do it too or not i dont know anyway i dont know what i write here but hey kelvin from the 
#future nice to see you.
#algorithm:
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    
    #TESTING AREA! 
    nums = [3, 3]
    target = 6
    result = sol.twoSum(nums, target)
    print("Result:", result)
