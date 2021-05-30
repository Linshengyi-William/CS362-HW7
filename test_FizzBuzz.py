import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_Fizz(self):
        result = FizzBuzz.FizzBuzz()
        for i in range(1,101):
            if i % 3 == 0:
                self.assertEqual("Fizz",result[i])

    def test_FizzBuzz(self):
        result = FizzBuzz.FizzBuzz()
        for  i in range(1,101):
            if i % 3 == 0 and i % 5 == 0:
                self.assertEqual("FizzBuzz",result[i])    
            elif i % 3 == 0:
                self.assertEqual("Fizz",result[i])
            elif i % 5 == 0:
                self.assertEqual("Buzz",result[i])  
            else:
                self.assertEqual(i,result[i])
                



if __name__ == '__main__':unittest.main()