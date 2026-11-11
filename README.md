# 🎲 Dice Game — Python OOP Project

A command-line dice game where a human player competes against the computer. The project demonstrates Python **object-oriented programming (OOP)** through three classes: `Die`, `Player`, and `DiceGame`.

## How the game works

- Both players start with a counter of **10**.
- Press **Enter** at each prompt to roll the dice for both players.
- Each roll produces a random integer from **1 to 6**.
- The player with the **higher roll wins the round**.
- The round winner's counter **decreases by 1**, and the loser's counter **increases by 1**.
- A tie leaves both counters unchanged.
- The game ends when either player's counter reaches **0**; that player is declared the winner.

> **Note:** The counter is not a conventional score: reaching zero wins. The game can take many rounds, and there is no maximum-round limit in the current implementation.

## Project structure

Keep these three files together:

```text
Dice-Game/
├── DiceGame.py       # Game loop, round logic, counters, winner detection
├── Player.py         # Player state and dice-roll behavior
├── Die.py            # Six-sided random dice roll
└── README.md         # Project documentation
```

| File | Class | Responsibility |
| --- | --- | --- |
| `Die.py` | `Die` | Rolls a six-sided die using Python's `random.randint(1, 6)` |
| `Player.py` | `Player` | Holds the player's name, die reference, and counter; updates the counter |
| `DiceGame.py` | `DiceGame` | Runs rounds, compares rolls, updates counters, and declares the winner |

## Requirements

- Python **3.9 or later** is recommended.
- A terminal or VS Code with the Python extension.
- **No third-party packages** are required; the project uses Python's standard library.

## How to run

1. Download or copy `DiceGame.py`, `Player.py`, and `Die.py` into the **same folder**.
2. Open that folder in VS Code, or open a terminal in the folder.
3. Check that Python is installed:

   ```bash
   python --version
   ```

4. Start the game:

   ```bash
   python DiceGame.py
   ```

   On systems where `python` is not available, try `python3 DiceGame.py` (macOS/Linux) or `py DiceGame.py` (Windows).

5. When prompted, press **Enter** to roll. Continue until a winner is announced.

**Important:** Run the command from the folder containing all three `.py` files. Although `DiceGame.py` also adds a `Dice_Game_PKG` path to Python's import search path, the straightforward supported layout is to keep the files together.

## Example console output

*Illustrative output; actual rolls and counters will vary.*

```text
-----------------------------
--🎲🎲-Starting the Dice game--🎲🎲----
-----------------------------
🎲🎲New round🎲🎲
Press any key to roll the die:
Player value -  5
Computer value -  2
Player won the round
Your counter :  9
Computer Counter :  11
***********************
```

## Program flow

```text
Start game
   |
Create Die, human Player, computer Player
   |
Prompt for next round
   |
Roll for both players
   |
Compare values
   |-- Human higher --> Human counter -1; computer counter +1
   |-- Computer higher --> Computer counter -1; human counter +1
   |-- Equal --> Counters unchanged
   |
Display counters
   |
Is either counter zero?
   |-- No --> Next round
   |-- Yes --> Announce winner and end
```

## OOP concepts demonstrated

- **Classes and objects:** `Die`, `Player`, and `DiceGame` represent distinct responsibilities.
- **Encapsulation:** Instance attributes such as `_counter` and `_die` store object state.
- **Properties:** `@property` exposes read access to values such as `counter`.
- **Composition:** Each `Player` references a `Die`, and `DiceGame` holds two `Player` objects.
- **Methods:** `roll()`, `play_round()`, `update_counters()`, and `check_game_over_fn()` divide behavior into reusable operations.
- **String representation:** `Player.__str__()` formats the winner announcement.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `ModuleNotFoundError: No module named 'Die'` or `'Player'` | Confirm all three Python files are in the same folder and run the command from that folder. |
| `python` command not found | Install Python and ensure it is on your PATH, or try `py` / `python3`. |
| Program appears to be waiting | The game is waiting for input; press **Enter**. |
| Game does not end quickly | This is possible under the current counter rules; rounds continue until a counter reaches zero. Use **Ctrl+C** to stop manually. |

## Current implementation notes

- The human and computer are both passed the **same `Die` instance**. Each call to `roll()` still generates a fresh random value, so the game can run as written.
- `Player.is_computer` refers to `_is_computer`, but the constructor does **not** assign that attribute (its assignment is commented out). The game does not currently access this property, so ordinary gameplay is unaffected; accessing the property directly would raise `AttributeError`.
- The prompt says “Press any key,” but Python's `input()` requires the user to press **Enter** to submit.
- This is an educational game, not a secure or competitive random-number system.

## Interview-ready summary

> I built a command-line dice game in Python to practice object-oriented design. I separated random dice generation, player state management, and game orchestration into three classes. Each round compares two random rolls and updates the players' counters. The game loop ends when one player's counter reaches zero. This helped me practice encapsulation, composition, methods, properties, and control flow.
