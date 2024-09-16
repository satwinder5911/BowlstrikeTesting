class BowlingGameV2:
    def __init__(self):
        # Initializing the rolls list to store the number of pins knocked down in each roll
        self.rolls = []
    
    def roll(self, pins):
        """
        Records the number of pins knocked down in a roll.
        
        Args:
            pins (int): The number of pins knocked down.
        """
        self.rolls.append(pins)
    
    def calculate_score(self):
        """
        Calculates the total score for the bowling game based on the rules.
        
        Returns:
            int: Total score of the game.
        """
        total_score = 0
        current_roll = 0
        
        # Iterate over 10 frames
        for frame in range(10):
            if self.is_strike(current_roll):  # Strike scenario
                total_score += 10 + self.strike_bonus(current_roll)
                current_roll += 1  # Move to the next frame
            elif self.is_spare(current_roll):  # Spare scenario
                total_score += 10 + self.spare_bonus(current_roll)
                current_roll += 2  # Skip to the next frame
            else:  # Open frame scenario
                total_score += self.frame_total(current_roll)
                current_roll += 2  # Move to the next frame
        
        return total_score
    
    def is_strike(self, roll_index):
        """
        Checks if the current roll is a strike (all pins knocked down in one roll).
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[roll_index] == 10
    
    def strike_bonus(self, roll_index):
        """
        Calculates the bonus for a strike (the next two rolls).
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            int: Bonus points for a strike.
        """
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
    
    def is_spare(self, roll_index):
        """
        Checks if the current frame is a spare (all pins knocked down in two rolls).
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            bool: True if the frame is a spare, False otherwise.
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    def spare_bonus(self, roll_index):
        """
        Calculates the bonus for a spare (the next roll).
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            int: Bonus points for a spare.
        """
        return self.rolls[roll_index + 2]
    
    def frame_total(self, roll_index):
        """
        Calculates the total score for a frame (two rolls).
        
        Args:
            roll_index (int): The index of the current roll in the rolls list.
        
        Returns:
            int: Total score for the frame.
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
