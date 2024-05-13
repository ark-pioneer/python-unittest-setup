import unittest

from greeter import greet


class TestGreet(unittest.TestCase):
    def test_sayHello(self):
        self.assertEqual(greet.sayHello("Ed"), "hello, Ed")

    def test_sayHelloTwice(self):
        self.assertEqual(greet.sayHelloNTimes("Ed", 2), "hello hello Ed")


if __name__ == "__main__":
    unittest.main()
