import unittest
import datetime


def my_brand(ass_name):
    s="=*=*=*= Manoj Kumar Reddy Buthukuri =*=*=*="+"\n"+"=*=*=*= Course 2023S-SSW567-WS =*=*=*= "+"\n"+"=*=*=*= "+ass_name+" =*=*=*= " +"\n"+"=*=*=*= "+str(datetime.datetime.now())+" =*=*=*= "
    return s


class TestMyBrand(unittest.TestCase):
    def test_my_brand(self):
        self.assertEqual(my_brand("HW1"),"=*=*=*= Manoj Kumar Reddy Buthukuri =*=*=*="+"\n"+"=*=*=*= Course 2023S-SSW567-WS =*=*=*= "+"\n"+"=*=*=*= HW1 =*=*=*= " +"\n"+"=*=*=*= "+str(datetime.datetime.now())+" =*=*=*= ")


unittest.main(argv=[''], verbosity=1, exit=False);
print("Hello World")
