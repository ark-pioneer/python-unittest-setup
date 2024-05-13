import unittest

from todo import todo


class TestTodo(unittest.TestCase):
    def setUp(self):
        self.todo = todo.Todo("A fantastic test todo", False)

    def test_todo_has_text(self):
        self.assertEqual(self.todo.text, "A fantastic test todo")


if __name__ == "__main__":
    unittest.main()
