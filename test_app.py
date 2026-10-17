import unittest
from app import app

class TestTasksAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Mini Tasks API is running!", response.data)

    def test_list_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            [
                "Python uygulamasini yaz",
                "Azure Pipeline kur",
                "Docker ogren"
            ]
        )

if __name__ == "__main__":
    unittest.main()