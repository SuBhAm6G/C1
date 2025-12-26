import random

def get_dice_visual(roll):
    """
    Returns an ASCII art representation of a single die roll.
    """
    if roll == 1:
        return "┌───────┐\n│       │\n│   ●   │\n│       │\n└───────┘"
    elif roll == 2:
        return "┌───────┐\n│ ●     │\n│       │\n│     ● │\n└───────┘"
    elif roll == 3:
        return "┌───────┐\n│ ●     │\n│   ●   │\n│     ● │\n└───────┘"
    elif roll == 4:
        return "┌───────┐\n│ ●   ● │\n│       │\n│ ●   ● │\n└───────┘"
    elif roll == 5:
        return "┌───────┐\n│ ●   ● │\n│   ●   │\n│ ●   ● │\n└───────┘"
    elif roll == 6:
        return "┌───────┐\n│ ●   ● │\n│ ●   ● │\n│ ●   ● │\n└───────┘"
    return ""

def roll_dice(num_dice, num_sides):
    """
    Simulates rolling multiple dice.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.

    Returns:
        list: A list containing the results of each die roll.
    """
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

if __name__ == "__main__":
    print("Welcome to the Multiple Dice Roller!")

    try:
        num_dice_input = int(input("How many dice do you want to roll? "))
        num_sides_input = int(input("How many sides does each die have? "))

        if num_dice_input <= 0 or num_sides_input <= 0:
            print("Please enter positive numbers for the number of dice and sides.")
        else:
            rolls = roll_dice(num_dice_input, num_sides_input)
            print(f"\nRolling {num_dice_input} dice with {num_sides_input} sides each:")
            for roll in rolls:
                if num_sides_input == 6: # Only show visual for standard 6-sided dice
                    print(f"\nDie Roll: {roll}\n{get_dice_visual(roll)}")
            print(f"Results: {rolls}")
            print(f"Total: {sum(rolls)}")
    except ValueError:
        print("Invalid input. Please enter whole numbers.")