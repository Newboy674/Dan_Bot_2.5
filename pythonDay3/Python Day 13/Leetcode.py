

class Solution:

    @classmethod     #WHY DID This FIX EVERYTHING whAT

    def twoSum(self, nums, target):  # -> List[int]:
            number_order1 = -1
            for number in nums:
                    number1 = number
                    number_order1 = number_order1 + 1
                    number_order2 = -1
                    for number in nums:   #Makes it skip first iteration to avoid duplicate counting (counting the same number in same spot)
                            number2 = number
                            number_order2 = number_order2 + 1

                            if number1 + number2 == target and number_order1 != number_order2:
                                result = [number_order1, number_order2]
                                return result





test_number_list=[3,2,4]
target = 6

Result = Solution.twoSum(test_number_list, target)

print(Result)


