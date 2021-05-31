import unittest
import leapYear


class TestCase(unittest.TestCase):
    def test_isLeapYear(self):
        year = 2000
        result = leapYear.leapYear(year)
        if (year % 4) == 0:  
            if (year % 100) == 0:  
                if (year % 400) == 0:  
                    self.assertEqual(result, True)
                else:  
                    self.assertEqual(result, False)
            else:  
                self.assertEqual(result, True)
        else:  
            self.assertEqual(result, False)

    
                



if __name__ == '__main__':unittest.main()