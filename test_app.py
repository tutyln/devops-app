
import unittest
from app import add_task, list_tasks, tasks

class TestTasks(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        add_task("Azure DevOps ogren")
        self.assertEqual(list_tasks(), ["Azure DevOps ogren"])

    def test_multiple_tasks(self):
        add_task("Python")
        add_task("Docker")
        self.assertEqual(len(list_tasks()), 2)

if __name__ == "__main__":
    unittest.main()
