import json
import unittest
from app import app

class TestCheckNumberEndpoint(unittest.TestCase):

    def test_check_number_valid_high(self):
        # Create a test client using the Flask application
        with app.test_client() as client:
            # Define a test payload with a high integer value
            payload = {"integer": 150}
            # Send a POST request to the /check_number endpoint with the test payload
            response = client.post("/check_number", json=payload)
            # Load the response data as JSON
            data = json.loads(response.data)
            # Assert that the result is correct
            self.assertEqual(data["integer"], "high")
    
    def test_check_number_valid_low(self):
        # Create a test client using the Flask application
        with app.test_client() as client:
            # Define a test payload with a low integer value
            payload = {"integer": 50}
            # Send a POST request to the /check_number endpoint with the test payload
            response = client.post("/check_number", json=payload)
            # Load the response data as JSON
            data = json.loads(response.data)
            # Assert that the result is correct
            self.assertEqual(data["integer"], "low")
    
    def test_check_number_missing_integer_parameter(self):
        # Create a test client using the Flask application
        with app.test_client() as client:
            # Define a test payload with a missing "integer" key
            payload = {"notinteger": "blah"}
            # Send a POST request to the /check_number endpoint with the test payload
            response = client.post("/check_number", json=payload)
            # Load the response data as JSON
            data = json.loads(response.data)
            # Assert that the error message is correct
            self.assertEqual(data["error"], "Missing integer parameter")
            # Assert that the status code is 400 (Bad Request)
            self.assertEqual(response.status_code, 400)
    
    def test_check_number_invalid_integer_value(self):
        # Create a test client using the Flask application
        with app.test_client() as client:
            # Define a test payload with an invalid integer value
            payload = {"integer": "abcd"}
            # Send a POST request to the /check_number endpoint with the test payload
            response = client.post("/check_number", json=payload)
            # Load the response data as JSON
            data = json.loads(response.data)
            # Assert that the error message is correct
            self.assertEqual(data["error"], "Invalid integer value")
            # Assert that the status code is 400 (Bad Request)
            self.assertEqual(response.status_code, 400)

    def test_check_number_regression(self):
        # Define a list of test payloads to test
        test_payloads = [
            {"integer": 150},
            {"integer": 50},
            {"notinteger": "blah"},
            {"integer": "abcd"}
        ]
        # Create a test client using the Flask application
        with app.test_client() as client:
            # Iterate over the test payloads and test the /check_number endpoint with each one
            for payload in test_payloads:
                # Send a POST request to the /check_number endpoint with the test payload
                response = client.post("/check_number", json=payload)
                # Load the response data as JSON
                data = json.loads(response.data)
                # Check the format of the response and verify that it contains the expected values
                if "integer" in data:
                    self.assertIn(data["integer"], ["high", "low"])
                elif "error" in data:
                    self.assertIn(data["error"], ["Missing integer parameter", "Invalid integer value"])
                else:
                    self.fail("Invalid response format")

