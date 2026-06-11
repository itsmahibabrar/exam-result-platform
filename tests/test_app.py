import unittest

from app import create_app


class AppFactoryTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_results_boilerplate_endpoint(self):
        response = self.client.get("/api/results/")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertIn("message", payload)
        self.assertIn("endpoints", payload)


if __name__ == "__main__":
    unittest.main()
