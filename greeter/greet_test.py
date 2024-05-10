import unittest

import greet

class TestGreet(unittest.TestCase):
    def test_sayHello(self):
      self.assertEqual(greet.sayHello('Ed'), 'hello, Ed')

if __name__ == '__main__':
  unittest.main()