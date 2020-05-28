class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        output = [0,0]
        for digit in range(len(nums)):
            difference = target - nums[digit]
            if difference not in hashmap:
                hashmap[nums[digit]] = digit
            else:
                output[0] = hashmap[difference]
                output[1] = digit
                return output