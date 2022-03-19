class Solution:
    @classmethod
    def isPalindrome(self, x: int):

        iteration = 0

        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True

        number_list = [int(number) for number in str(x)]
        number_inverted = number_list[:]
        number_inverted.reverse()

        for number in number_list:

            iteration = iteration + 1

            numbera = number_inverted[iteration - 1]
            numberb = number_list[iteration - 1]

            if numbera != numberb:
                return False
            if iteration == len(number_list):
                return True




answer = Solution.isPalindrome(121)
print(answer)

# I DID IT!!!