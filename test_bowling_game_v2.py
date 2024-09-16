import unittest
from bowling_game_v2 import BowlingGameV2

class TestBowlingGameV2(unittest.TestCase):
    
    def setUp(self):
        """Sets up a new BowlingGameV2 instance before each test."""
        self.game = BowlingGameV2()
    
    def roll_many(self, num_rolls, pins):
        """Helper function to roll a specified number of times with the same number of pins."""
        for _ in range(num_rolls):
            self.game.roll(pins)
    
    def roll_strike(self):
        """Helper function to roll a strike (10 pins in one roll)."""
        self.game.roll(10)
    
    def roll_spare(self):
        """Helper function to roll a spare (5 pins, then 5 pins)."""
        self.game.roll(5)
        self.game.roll(5)
    
    def test_gutter_game(self):
        """Test that a game with all gutter balls results in a score of 0."""
        self.roll_many(20, 0)  # 20 rolls of 0 pins
        self.assertEqual(self.game.calculate_score(), 0)
    
    def test_all_ones(self):
        """Test a game where each roll knocks down 1 pin."""
        self.roll_many(20, 1)  # 20 rolls of 1 pin each
        self.assertEqual(self.game.calculate_score(), 20)
    
    def test_single_spare(self):
        """Test that a single spare is scored correctly."""
        self.roll_spare()  # Roll a spare
        self.game.roll(3)  # Roll 3 pins in the next frame
        self.roll_many(17, 0)  # Remaining rolls are gutter balls
        self.assertEqual(self.game.calculate_score(), 16)
    
    def test_single_strike(self):
        """Test that a single strike is scored correctly."""
        self.roll_strike()  # Roll a strike
        self.game.roll(4)  # Roll 4 pins in the next frame
        self.game.roll(3)  # Roll 3 pins in the next frame
        self.roll_many(16, 0)  # Remaining rolls are gutter balls
        self.assertEqual(self.game.calculate_score(), 24)
    
    def test_perfect_game(self):
        """Test that a perfect game (12 strikes) results in a score of 300."""
        self.roll_many(12, 10)  # 12 strikes
        self.assertEqual(self.game.calculate_score(), 300)
    
    def test_open_frame(self):
        """Test that an open frame (less than 10 pins knocked down) is scored correctly."""
        self.game.roll(5)  # Roll 5 pins
        self.game.roll(4)  # Roll 4 pins (open frame)
        self.roll_many(18, 0)  # Remaining rolls are gutter balls
        self.assertEqual(self.game.calculate_score(), 9)
    
    def test_tenth_frame_strike(self):
        """Test that the 10th frame's bonus rolls after a strike are handled correctly."""
        self.roll_many(18, 0)  # 18 gutter balls
        self.roll_strike()  # Strike in the 10th frame
        self.game.roll(10)  # Bonus roll 1
        self.game.roll(10)  # Bonus roll 2
        self.assertEqual(self.game.calculate_score(), 30)

if __name__ == '__main__':
    unittest.main()
