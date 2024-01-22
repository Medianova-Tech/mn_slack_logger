import unittest
from unittest.mock import patch
from mn_slack_logger import SlackLogger


class TestSlackLogger(unittest.TestCase):

    def setUp(self):
        # Create an instance of SlackLogger with a fake Slack URL and user
        self.logger = SlackLogger(slack_url="https://fake-slack-webhook-url", slack_user="TestLogger")

    @patch('requests.Session.post')
    def test_log_error(self, mock_post):
        # Call the log method with an error message
        self.logger.log("Test error message", level="error", error="Test error traceback")

        # Verify that the session.post method was called once
        mock_post.assert_called_once()

        # Check the content of the sent data
        _, called_kwargs = mock_post.call_args
        payload = called_kwargs['json']
        self.assertIn("attachments", payload)
        self.assertEqual(payload["attachments"][0]["color"], "danger")
        self.assertEqual(payload["attachments"][0]["text"], "Test error message")

        # Display the logger payload and a success message
        print("Error Logger Payload:")
        print(payload)
        print("Test log_error: PASSED")

    @patch('requests.Session.post')
    def test_log_warning(self, mock_post):
        # Call the log method with a warning message
        self.logger.log("Test warning message", level="warning")

        # Verify that the session.post method was called once
        mock_post.assert_called_once()

        # Check the content of the sent data
        _, called_kwargs = mock_post.call_args
        payload = called_kwargs['json']
        self.assertIn("attachments", payload)
        self.assertEqual(payload["attachments"][0]["color"], "warning")
        self.assertEqual(payload["attachments"][0]["text"], "Test warning message")

        # Display the logger payload and a success message
        print("Warning Logger Payload:")
        print(payload)
        print("Test log_warning: PASSED")

    @patch('requests.Session.post')
    def test_log_info(self, mock_post):
        # Call the log method with an info message
        self.logger.log("Test info message", level="info")

        # Verify that the session.post method was called once
        mock_post.assert_called_once()

        # Check the content of the sent data
        _, called_kwargs = mock_post.call_args
        payload = called_kwargs['json']
        self.assertIn("attachments", payload)
        self.assertEqual(payload["attachments"][0]["color"], "good")
        self.assertEqual(payload["attachments"][0]["text"], "Test info message")

        # Display the logger payload and a success message
        print("Info Logger Payload:")
        print(payload)
        print("Test log_info: PASSED")

    def test_shorten_traceback(self):
        # Test the shorten_traceback method with a long traceback
        long_traceback = "This is a very long traceback\n" * 50
        max_length = 1000  # Adjust this value based on your desired limit
        shortened_traceback = self.logger.shorten_traceback(long_traceback)

        # Check if the length of the shortened traceback is within the updated limit
        self.assertLessEqual(len(shortened_traceback), max_length)

        # Display the shortened traceback and a success message
        print("Shortened Traceback:")
        print(shortened_traceback)
        print("Test shorten_traceback: PASSED")

    def test_build_fields(self):
        # Call the _build_fields method with sample data
        level = "error"
        url = "https://example.com"
        params = {"param1": "value1", "param2": "value2"}
        headers = {"Header1": "Value1", "Header2": "Value2"}
        error = "Sample traceback text"
        fields = self.logger._build_fields(level, url, params, headers, error)

        # Check if the fields list is correctly built
        expected_fields = [
            self.logger.field_maker("Level", level),
            self.logger.field_maker("Url", url),
            self.logger.field_maker("Parameters", params),
            self.logger.field_maker("Headers", headers),
            self.logger.field_maker("Exception", self.logger.shorten_traceback(error))
        ]
        self.assertEqual(fields, expected_fields)

        # Display the fields and a success message
        print("Fields:")
        for field in fields:
            print(field)
        print("Test build_fields: PASSED")

    def test_field_maker(self):
        # Call the field_maker method with sample title and value
        title = "Sample Title"
        value = "Sample Value"
        field = self.logger.field_maker(title, value)

        # Check if the field is correctly built
        expected_field = {
            "title": title,
            "value": f"``` {value} ```",
            "short": False
        }
        self.assertEqual(field, expected_field)

        # Display the field and a success message
        print("Field:")
        print(field)
        print("Test field_maker: PASSED")


if __name__ == '__main__':
    unittest.main()
