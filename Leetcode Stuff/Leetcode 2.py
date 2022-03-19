##https://leetcode.com/problems/roman-to-integer/

class romanvalue:
    def __init__(self, symbol):
        self.Symbol = symbol

    def value(self):
        if "I" in self.symbol:
         absolute_value = 1
        if "V" in self.symbol:
         absolute_value = 5
        if "X" in self.symbol:
            absolute_value = 10
        if "L" in self.symbol:
          absolute_value = 50
        if "C" in self.symbol:
          absolute_value = 100
        if "D" in self.symbol:
           absolute_value = 500
        if "M" in self.symbol:
          absolute_value = 1000
        return absolute_value



class Solution:
    @classmethod
    def Roman(self, s):
        Answer = 0

        if "M" in s:

        if "D" in s:

        if "C" in s:

        if "L" in s:

        if "X" in s:

        if "V" in s:

            V_counter = s.count("V")

            V_tuple = s.partition(s)

            V_before = V_tuple[0]

            V_after = V_tuple[2]


        if "I" in s:

           I_tuple = s.partition(I)


        return Answer


#Test

Ans = Solution.Roman("LIIIV")

print(Ans)


##given up, a case of "MCMXCIV" confused me, as the mcm wont work wif me code
