Python Documentation for Bowling Game Backend 

Introduction
This document provides Python-style documentation for the backend logic of the Bowling Game (V2). The BowlingGameV2 class handles the scoring and logic for a standard 10-pin bowling game, including the handling of strikes, spares, and open frames.
Class: BowlingGameV2
This class implements the core functionality of a 10-pin bowling game. It provides methods to record rolls, calculate the score, and handle special cases such as strikes and spares.
Methods:
__init__(self)
Initializes the bowling game by creating an empty list to store the number of pins knocked down in each roll.

Args: None
Returns: None
roll(self, pins)
Records the number of pins knocked down in a roll and adds it to the rolls list.

Args:
    pins (int): The number of pins knocked down in a single roll.

Returns: None
calculate_score(self)
Calculates the total score for the game based on the number of pins knocked down and the rules of bowling. It correctly handles the bonuses for strikes and spares and calculates the final score after 10 frames.

Args: None
Returns:
      total_score (int): The total score for the game after all frames have been played.
is_strike(self, roll_index)
Determines whether the roll at the given index is a strike (all 10 pins knocked down in one roll).

Args:
   roll_index (int): The index of the current roll in the rolls list.
Returns:
   bool: Returns True if the roll is a strike (10 pins in one roll), otherwise False.
strike_bonus(self, roll_index)
Calculates the bonus for a strike. The bonus is the sum of the pins knocked down in the next two rolls after the strike.

Args:
  roll_index (int): The index of the current roll in the rolls list.
Returns:
  bonus (int): The bonus points for the strike, calculated as the sum of the next two rolls.
is_spare(self, roll_index)
Determines whether the current frame is a spare (all 10 pins knocked down in two rolls).

Args:
  roll_index (int): The index of the current roll in the rolls list.
Returns:
  bool: Returns True if the frame is a spare (10 pins in two rolls), otherwise False.
spare_bonus(self, roll_index)
Calculates the bonus for a spare. The bonus is the number of pins knocked down in the next roll after the spare.

Args:
  roll_index (int): The index of the current roll in the rolls list.
Returns:
  bonus (int): The bonus points for the spare, calculated as the number of pins knocked down in the next roll.
frame_total(self, roll_index)
Calculates the total score for a frame. This is the sum of the two rolls in the current frame.

Args:
  roll_index (int): The index of the current roll in the rolls list.
Returns:
  total (int): The total number of pins knocked down in the frame.
Example Usage
To use the BowlingGameV2 class:

1. Initialize an instance of BowlingGameV2.
2. Use the roll() method to record each roll.
3. After all rolls are completed, call calculate_score() to get the total score for the game.

Example:


game = BowlingGameV2()
game.roll(10)  # Roll a strike
game.roll(3)
game.roll(4)
total_score = game.calculate_score()
print(f'Total score: {total_score}')

