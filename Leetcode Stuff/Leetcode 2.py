https://leetcode.com/problems/roman-to-integer/


@classmethod
class Solution:

    def romanToInt(self, s):
        value = 0

        if "M" in s:


            value = value + 1000


        if "V" in s:

        elif "VI" in s:
        elif "VII" in s:

        else:

            value = value + 5

        return Answer






#Test



Answer = Solution.romanToInt("LVIII")

print(Awnser)
