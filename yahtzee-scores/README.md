# Project - Yahtzee Scores

In this project, you'll implement the scoring rules for the dice game Yahtzee. You'll be given a roll of five dice and asked to work out what every scoring category is worth, then apply a chosen category to a scorecard.

## Project Overview

Yahtzee is played by rolling five six-sided dice (players get up to three rolls per turn, keeping any dice they like between rolls — that part isn't in scope here) and then assigning the result to one of thirteen scoring categories on a scorecard. Each category can only be used once per game.

The upper section scores the total of one specific face value:

- Ones, Twos, Threes, Fours, Fives, Sixes: sum of the dice showing that number.

The lower section scores specific patterns:

- Three of a Kind: sum of all five dice, if at least three show the same value.
- Four of a Kind: sum of all five dice, if at least four show the same value.
- Full House: 25 points, if the dice show exactly three of one value and two of another.
- Small Straight: 30 points, if the dice contain four consecutive values (e.g. 2-3-4-5).
- Large Straight: 40 points, if the dice contain five consecutive values (e.g. 1-2-3-4-5).
- Yahtzee: 50 points, if all five dice show the same value.
- Chance: sum of all five dice, always available.

Any category that isn't satisfied by a roll still exists, it just scores 0 if chosen — a category is always available, whether or not choosing it is a good idea. (We won't implement the official upper-section bonus, joker rules for extra Yahtzees, or the "roll again" mechanics — just scoring one finished roll.)

We'll represent a roll as a string of five digits, e.g. `33356` for the dice `[3, 3, 3, 5, 6]`, and a scorecard as a mapping from category name to either a score, or `None` if that category hasn't been used yet. The thirteen category names are given for you in `yahtzee.py` as `CATEGORIES`.

## Project Requirements

- Implement a function that parses a roll string into a convenient representation.
- Implement a function that computes the score every category would give for a roll (whether or not that category has already been used).
- Implement a function that applies a chosen category and score to a scorecard, returning the new scorecard.

## Notes on teamwork

Your team needs to decide how a roll and a scorecard will be represented in Python before splitting up the work — this is the core decision everybody depends on. Explore this with your team first, writing some test code together. It would be a mistake to split up the work before agreeing on the data model.

Once that's settled, here's a natural way to split the thirteen categories across six people:

1. The whole upper section (Ones through Sixes) — one person, since it's the same logic parameterized by face value.
2. Three of a Kind and Four of a Kind.
3. Full House.
4. Small Straight and Large Straight.
5. Yahtzee.
6. Chance, plus wiring `generate_scores` and `apply_score` together once everyone else's category functions exist.

Start with the upper section or Yahtzee, since they're the simplest — that will exercise your shared roll representation before tackling the trickier cases. Leave Full House and the straights until your shared representation is solid, since they need to look at counts and runs rather than a single value.

## How you'll be assessed

- **Correctness**: Your code should produce the correct output for all test cases.
- **Comprehension**: _Everybody_ should understand _all_ the code in the project.
- **Quality**: We'd like to see a data model that supports the functionality well, and sensible utilization of the Python features you learned throughout the bootcamp.

## How to run the tests

To run the tests, you can configure your IDE to run unittest tests in the "." directory. Alternatively, you can run the tests from the command line using the following command:

```bash
python -m unittest test_yahtzee.py
```

## Try Playing Yahtzee!


Check out [Yahtzee](https://cardgames.io/yahtzee/).

