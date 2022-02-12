

class Solution:

    @classmethod     #WHY DID This FIX EVERYTHING whAT

    def twoSum(self, nums, target):  # -> List[int]:

            for number in nums:
                    number1 = number
                    number_order1 = nums.index(number)

                    for number in nums:
                            number2 = number
                            number_order2 = nums.index(number)

                            if number_order1 != number_order2 and number1 + number2 == target or number1 == number2 and [[number_order1 != number_order2]]:
                                result = [number_order1, number_order2]
                                return result





test_number_list=[4,4,6,2]
target = 8

Result = Solution.twoSum(test_number_list, target)

print(Result)


