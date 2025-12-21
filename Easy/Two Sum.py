class Solution:
    def twoSum(self, input: list[int], target: int) -> list[int]:

        lookup = {}
        for i, num in enumerate(input):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i

sol = Solution()
input = [2, 7, 11, 15]
target = 9

print(sol.twoSum(input, target))
