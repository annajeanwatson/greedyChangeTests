## Anna Watson
## CSCI232 Program 3 - 2
## This program implements a greedy algorithm to calculate a requested output using 
## a given denomination of coins. The program also tests the greedy algorithm from
## the MyTest class.

import unittest

class Greedy:
    def __init__(self, amount, coins):
        self.amount = amount
        self.coins = coins      
        
    def greedy(self):
        if(self.amount < 0):
            print("Input cannot be negitive.")
            return 0
        else:
            answer = []
            try:
                while (self.amount > 0):
                    if (self.amount >= self.coins[0]):
                        num = self.amount // self.coins[0]
                        self.amount -= (num * self.coins[0])
                        answer.append([self.coins[0], num])
                    self.coins = self.coins[1:]
                print(answer)
                return answer
            except:
                print("Coins sent into are empty.")
                return 0

class MyTest(unittest.TestCase):
    
    def test(self):
        """test a normal result"""
        self.assertEqual(Greedy(47, [25,10,5,1]).greedy(), [[25, 1], [10, 2], [1, 2]])
        """test a normal result"""
        self.assertEqual(Greedy(5, [25,10,5,1]).greedy(), [[5,1]])
        """test if requested number is negitive"""
        self.assertEqual(Greedy(-2, [25,10,5,1]).greedy(), 0)
        """test if no coins are entered"""
        self.assertEqual(Greedy(25, [0]).greedy(), 0)
        
test = MyTest()
print("If none is returned, the test cases hold")
print("")
print(test.test())
print("")

