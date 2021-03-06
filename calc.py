import unittest


def add(x,y):
    return x+y

def pow(x,y):
    if y == 0:
        return 1
    else:
        return x*pow(x,y-1)

def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

class calcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,5),8)
    def test_subtract(self):
        self.assertEqual(subtract(10,3),7)
    def test_pow(self):
        self.assertEqual(pow(2,4),16)
        self.assertEqual(pow(3,5),243)
    def test_divide(self):
        self.assertEqual(divide(6,2),3)
        
if __name__ == '__main__':
    unittest.main()
