import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    def setUp(self):
        self.home_win = {"home_score": 3, "away_score": 2}
        self.away_win = {"home_score": 0, "away_score":2}
        self.draw = {"home_score": 1, "away_score": 1}
        self.final_scores = [self.home_win, self.away_win, self.draw]

    def test_get_home_win_when_home_score_higher(self): 
        self.assertEqual("Home win", get_result(self.home_win))

    def test_get_away_win_when_away_score_higher(self):
        self.assertEqual("Away win", get_result(self.away_win))

    def test_get_draw_when_scores_are_the_same(self):
        self.assertEqual("Draw", get_result(self.draw))    

    def test_get_final_scores(self):
        self.assertEqual(["Home win", "Away win", "Draw"], get_result(self.final_scores))

   
   
    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
