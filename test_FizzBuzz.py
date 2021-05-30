import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_Fizz(self):
        result = FizzBuzz.FizzBuzz()
        for i in len(result):
            if i % 3 == 0:
                self.assertEqual("Fizz",result[i])





if __name__ == '__main__':unittest.main()