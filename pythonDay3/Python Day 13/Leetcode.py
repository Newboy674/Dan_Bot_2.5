##https://leetcode.com/problems/two-sum/discuss/1754104/Not-the-most-efficient-but-very-easy-to-understand-in-Java


def twoSum( nums, target):
        number_order1 = -1
        number_order2 = -1

        for number in nums:
            number_order1 = number_order1 + 1
            number1 = number
            number_order2 = -1      #Resets second number

            for number in nums:
                number_order2 = number_order2 + 1
                number2 = number

                if number1 + number2 == target:
                    result = [number_order1, number_order2]
                    return result






test_number_list=[5, 7, 2, 9]
target = 11

Result = twoSum(test_number_list, target)

print(Result)
