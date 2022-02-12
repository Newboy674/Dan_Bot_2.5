##https://leetcode.com/problems/two-sum/submissions/

class Solution:

    @classmethod     #WHY DID This FIX EVERYTHING whAT

    def twoSum(self, nums, target):  # -> List[int]:

            for number in nums:
                    number1 = number
                    number_order1 = nums.index(number)

                    for number in nums:
                            number2 = number
                            number_order2 = nums.index(number)

                            if number1 + number2 == target and number_order1 != number_order2:
                                result = [number_order1, number_order2]
                                return result





test_number_list=[3,2,4,6]
target = 6

Result = Solution.twoSum(test_number_list, target)

print(Result)


