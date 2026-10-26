
"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import patch

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test dominant emotion detection."""

    @patch("emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04,
                }
            }]
        }
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.90,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.01,
                    "sadness": 0.04,
                }
            }]
        }
        result = emotion_detector("I am very angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("emotion_detection.requests.post")
    def test_fear(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.02,
                    "disgust": 0.03,
                    "fear": 0.85,
                    "joy": 0.04,
                    "sadness": 0.06,
                }
            }]
        }
        result = emotion_detector("I am afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.02,
                    "disgust": 0.03,
                    "fear": 0.04,
                    "joy": 0.01,
                    "sadness": 0.90,
                }
            }]
        }
        result = emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.02,
                    "disgust": 0.90,
                    "fear": 0.03,
                    "joy": 0.01,
                    "sadness": 0.04,
                }
            }]
        }
        result = emotion_detector("That is disgusting")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()
