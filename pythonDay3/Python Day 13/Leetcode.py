##https://leetcode.com/problems/two-sum/submissions/
class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self, nums, target):  # -> List[int]:
            number_order1 = -1
            number_order2 = -1

            for number in nums:
                    number_order1 = number_order1 + 1
                    number1 = number

                    for number in nums:
                            number_order2 = number_order2 + 1
                            number2 = number

                            if number1 + number2 == target:
                                result = [number_order1, number_order2]
                                return result




solution = Solution()      #This took a while to add holy... makes the class a callable

test_number_list=[5, 7, 2, 9]
target = 11

Result = solution.twoSum(test_number_list, target)

print(Result)
