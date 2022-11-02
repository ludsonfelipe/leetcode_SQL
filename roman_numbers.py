# My firsts
class Solution:
    def romanToInt(self, s: str) -> int:
        
        increment = 0
        
        decrement = 0
        
        numbers = []

        dicio = {
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
                }
        
        for letter in s:
            numbers.append(dicio[letter])
        soma = sum(numbers)

        for c in range(len(numbers)):
            if c+1 <= len(numbers)-1:            
                if numbers[c+1]>numbers[c]:
                    increment += (numbers[c+1]-numbers[c])
                    decrement += (numbers[c+1]+numbers[c])
        soma -= decrement
        soma += increment

        return soma

# Best
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total, prev = 0, 0
        for c in reversed(s):
            if romans[c] < prev:
                total -= romans[c]
            else:
                total += romans[c]
            prev = romans[c]
        return total