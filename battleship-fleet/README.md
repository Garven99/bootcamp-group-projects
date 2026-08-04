# Project - Battleship Fleet

In this project, you'll implement shot resolution for a single player's board in Battleship. You'll be given a fleet layout and a history of shots already fired, and asked to work out which cells are still legal to fire at, and what happens when you fire at one.

## Project Overview

Battleship is played on a 10x10 grid, with columns `A`-`J` and rows `1`-`10` (e.g. `A1`, `J10`). One player's fleet consists of five ships, each occupying a straight line of adjacent cells:

- **Carrier**: 5 cells
- **Battleship**: 4 cells
- **Cruiser**: 3 cells
- **Submarine**: 3 cells
- **Destroyer**: 2 cells

Firing at a cell is a **hit** if it belongs to any ship, or a **miss** otherwise. Once every cell belonging to a ship has been hit, that ship is **sunk**. Once every ship in the fleet is sunk, the fleet is **defeated**. You can't fire at a cell that's already been fired at (whether it was a hit or a miss), and you can't fire off the edge of the board.

For this project, you need to implement handling for all of this: legal shots, hits, misses, sinking a ship, and defeating the fleet.

We'd like a convenient text notation for describing a board's state, similar in spirit to chess's FEN. A state is written as two fields separated by `|`: the fleet, and the shots fired so far.

```
carrier:A1,A2,A3,A4,A5;destroyer:C5,C6 | A1,B7
```

This means: the carrier occupies `A1`-`A5`, the destroyer occupies `C5` and `C6`, and two shots have been fired so far — `A1` (a hit on the carrier) and `B7` (a miss). `COLUMNS`, `ROWS`, `BOARD_CELLS`, and `FLEET` are provided for you in `battleship.py`.

## Project Requirements

- Implement a function that parses a board state string into a convenient representation.
- Implement a function that generates every cell that's still legal to fire at (every board cell that hasn't been fired at yet).
- Implement a function that applies a shot at a chosen cell, returning the resulting state along with whether it was a hit, a miss, or sank a ship, and whether the fleet has now been defeated. Firing at a cell that's already been fired at should not be allowed.

You do not need to implement the opponent's fleet, ship placement/validation, turn order, or a two-player game loop. Focus on: given one fleet and the shots fired so far, where can you still fire, and what happens when you do?

## Notes on teamwork

Your team needs to decide how a board state will be represented in Python before splitting up the work — this is the core decision everybody depends on. Explore this with your team first, writing some test code together. It would be a mistake to split up the work before agreeing on the data model.

Once that's settled, split up the work across five or six people:

1. Legal shots — every board cell that hasn't been fired at yet.
2. Hit or miss — does a cell belong to any ship?
3. Which ship — given a hit, which ship in the fleet does it belong to?
4. Sunk — has every cell of that ship now been fired at?
5. Fleet defeated — have all five ships been sunk?
6. `apply_shot`, wiring everyone else's checks together and rejecting a shot at a cell that's already been fired at or off the board.

Start with legal shots and hit-or-miss together, since every shot needs them and they don't depend on anything else. Save fleet defeated for last, since it depends on sunk detection being correct for every ship.

## How you'll be assessed

- **Correctness**: Your code should produce the correct output for all test cases.
- **Comprehension**: _Everybody_ should understand _all_ the code in the project.
- **Quality**: We'd like to see a data model that supports the functionality well, and sensible utilization of the Python features you learned throughout the bootcamp.

## How to run the tests

To run the tests, you can configure your IDE to run unittest tests in the "." directory. Alternatively, you can run the tests from the command line using the following command:

```bash
python -m unittest test_battleship.py
```

## Further Reading

Check out [Battleship (game)](https://en.wikipedia.org/wiki/Battleship_(game)) on Wikipedia for the classic rules this project is based on.

Check out [ How to Play Battleship](https://www.youtube.com/watch?v=q0qpQ8doUp8) video for a visual guide.
