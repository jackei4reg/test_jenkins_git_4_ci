from test_python import *
import unittest

class first_test(unittest.TestCase):
  def test_first_case(self):
    self.assertEqual(2, twonumberadd(1, 1))
    
  def test_second_case(self):
    self.assertEqual(3, twonumberadd(1, 1))