import unittest
from app import app
class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.client = app.test_client()
        self.client.testing = True

    def test_healthcheck(self):
        """Test the healthcheck endpoint."""
        response = self.client.get('/api/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Server is running!"})

if __name__ == '__main__':
    unittest.main()
