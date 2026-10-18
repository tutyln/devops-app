
import unittest
from unittest.mock import patch

from app import app


class TestTasksAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.content_type)

    @patch("app.get_db_connection")
    def test_list_tasks(self, mock_db):
        cursor = (
            mock_db.return_value
            .__enter__.return_value
            .cursor.return_value
            .__enter__.return_value
        )
        cursor.fetchall.return_value = [
            (1, "Python uygulamasini yaz"),
            (2, "Azure Pipeline kur"),
        ]

        response = self.client.get("/tasks")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            [
                {"id": 1, "title": "Python uygulamasini yaz"},
                {"id": 2, "title": "Azure Pipeline kur"},
            ],
        )

    @patch("app.get_db_connection")
    def test_create_task(self, mock_db):
        cursor = (
            mock_db.return_value
            .__enter__.return_value
            .cursor.return_value
            .__enter__.return_value
        )
        cursor.fetchone.return_value = (3, "Yeni görev")

        response = self.client.post(
            "/tasks",
            json={"title": "Yeni görev"},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.get_json(),
            {"id": 3, "title": "Yeni görev"},
        )

    def test_create_empty_task(self):
        response = self.client.post("/tasks", json={"title": "   "})

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
