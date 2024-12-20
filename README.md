# Number Guessing Game 🎲

A simple Python-based number guessing game where the player has to guess a randomly generated number within a given range and a limited number of attempts.

## How to Play

1. The program will randomly choose a number between `1` and `50`.
2. You have **5 attempts** to guess the number correctly.
3. After each incorrect guess, the program will give you a hint:
   - `Higher...` if your guess is too low.
   - `Lower...` if your guess is too high.
4. If you run out of attempts, the game will reveal the correct number.
5. After each game, you can choose to play again or exit.

---

## Features

- **Randomized Gameplay:** The number changes every round.
- **Hints Provided:** The program guides you with "Higher" or "Lower."
- **Input Validation:** Ensures only valid numbers are accepted.
- **Replay Option:** Allows you to play multiple rounds.

---

## Prerequisites

Make sure you have Python 3 installed. You can check by running:

```bash
python3 --version
