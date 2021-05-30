import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_Fizz(self):
        result = FizzBuzz.FizzBuzz()
        for i in range(len(result)):
            if i % 3 == 0:
                self.assertEqual("Fizz",result[i])

    def test_Buzz(self):
        result = FizzBuzz()
        for i in range(len(result)):
            if i % 5 == 0:
                self.assertEqual("Buzz", result[i])



if __name__ == '__main__':unittest.main()