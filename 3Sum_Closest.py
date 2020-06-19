class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        total = 0
        res = {}
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                print(total)
                if total == target:
                    return total
                elif total < target:
                    res[abs(total-target)] = total
                    left += 1
                elif total > target:
                    res[abs(total-target)] = total
                    right -= 1
        temp = min(res.keys())
        return res[temp]
                    