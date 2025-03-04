import unittest
from app import add

class TestApp(unittest.Testcase) :
    def Test_add(self) :
        self.asserEqual(add(2,3),5)
        self.asserEqual(add(2,4),6)
        self.asserEqual(add(2,5),7)
        self.asserEqual(add(2,6),8)


if __name__=="__main__" :
    unittest.main()
