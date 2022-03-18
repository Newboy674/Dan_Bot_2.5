##https://leetcode.com/problems/roman-to-integer/

class Solution:
    @classmethod
    def Roman(self, s):
        Answer = 0

        if "M" in s:

            Answer = Answer + 1000

        if "D" in s:
            Answer = Answer + 500

        if "C" in s:
            Answer = Answer + 100

        if "L" in s:
            Answer = Answer + 50

        if "X" in s:
            Answer = Answer + 10

        if "V" in s:
            V_counter = s.count("V")

            Answer = Answer + 5

        if "I" in s:

            I_counter = s.count("I")    #I_counter is equal to the amount of I's in the string (s)
            afterV = s.count ("VI")   #Will be 1 if after V, Will be 0 if not. This works because you cannot have "IVI" in roman numerals

            if I_counter == 1:
                Answer = Answer + 1

            elif I_counter != 1:

                if afterV == 1:
                    Answer = Answer + I_counter

                else:
                 Answer = Answer - I_counter

            return Answer


#Test

Ans = Solution.Roman("LIIIV")

print(Ans)
