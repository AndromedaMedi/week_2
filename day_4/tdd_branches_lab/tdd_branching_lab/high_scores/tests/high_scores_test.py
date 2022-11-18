import unittest

from src.high_scores import latest, personal_best, personal_top_three, high_to_low

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [3, 5, 8, 10, 4, 6]

    # Test latest score (the last thing in the list)

    def test_get_latest_score(self):
        expected_output = 6
        actual_output = latest(self.scores)
        self.assertEqual(expected_output, actual_output) 

    # Test personal best (the highest score in the list)
    
    def test_get_personal_score(self):
        expected_output = 10
        actual_output = personal_best(self.scores)
        self.assertEqual(expected_output, actual_output) 


    # Test top three from list of scores

    def test_get_top_three(self):
        expected_output = [6, 8, 10]
        actual_output = personal_top_three(self.scores)
        self.assertEqual(expected_output, actual_output)

    # Test ordered from highest to lowest

    def test_ordered_from_highest_to_lowest(self):
        expected_output = [10, 8, 6, 5, 4, 3]
        actual_output = high_to_low(self.scores)
        self.assertEqual(expected_output, actual_output)

    # Test top three when there is a tie

    def test_get_top_three_when_tie(self):
        new_scores = [4, 8, 8, 6, 10]
        expected_output = [8, 8, 10]
        actual_output = personal_top_three(new_scores)
        self.assertEqual(expected_output, actual_output)

    # Test top three when there are less than three

    def test_get_top_three_when_less_than_three(self):
        new_scores_2 = [4, 7]
        expected_output = [7, 4]
        actual_output = personal_top_three(new_scores_2)
        self.assertEqual(expected_output, actual_output)


    # Test top three when there is only one
    
    def test_get_top_three_when_less_than_three(self):
        new_scores_3 = [4]
        expected_output = [4]
        actual_output = personal_top_three(new_scores_3)
        self.assertEqual(expected_output, actual_output)