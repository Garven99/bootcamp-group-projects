# Project - Poker Hands

In this project, you'll implement hand ranking for five-card poker. You'll be given a hand of five cards and asked to work out which of the nine standard categories it belongs to, then compare two hands to see which one wins.

## Project Overview

Poker hands are ranked using a standard 52-card deck. Card ranks 2-10 are written as themselves, J/Q/K/A are worth their usual face ranks, and Ace can complete either the highest straight (10-J-Q-K-A) or the lowest (A-2-3-4-5). Suits don't have a ranking among themselves — a flush is a flush regardless of which suit it is.

There are nine hand categories, from weakest to strongest:

- **High Card**: no other category applies; ranked by the highest card, then the next, and so on.
- **Pair**: two cards of the same rank.
- **Two Pair**: two different pairs.
- **Three of a Kind**: three cards of the same rank.
- **Straight**: five cards with consecutive ranks, any suits.
- **Flush**: five cards of the same suit, any ranks.
- **Full House**: three of a kind plus a pair.
- **Four of a Kind**: four cards of the same rank.
- **Straight Flush**: five cards with consecutive ranks, all the same suit.

A hand always belongs to exactly one of these categories — the *best* one it qualifies for (a straight flush is not also counted separately as a flush and a straight).

We'd like a convenient text notation for describing a hand: five comma-separated cards, each written as rank followed by suit. A rank is `2`-`10`, `J`, `Q`, `K`, or `A`; a suit is `S`, `H`, `D`, or `C`. For example:

```
10S,10H,10D,KC,KS
```

This is a full house: three 10s and a pair of Kings. `RANK_ORDER`, `SUITS`, and `HAND_RANKS` are provided for you in `poker.py`.

## Project Requirements

- Implement a function that parses a hand string into a convenient representation.
- Implement a function that determines which of the nine categories a hand belongs to, along with enough information to break ties against another hand in the same category.
- Implement a function that compares two hands and reports which one wins (or whether it's a tie).

You do not need to implement dealing, betting, drawing/discarding, or comparing more than two hands at once. Focus on: given one finished hand, what category is it, and how does it compare to another hand?

## Notes on teamwork

Your team needs to decide how a hand and a classification will be represented in Python before splitting up the work — this is the core decision everybody depends on. Explore this with your team first, writing some test code together. It would be a mistake to split up the work before agreeing on the data model.

Once that's settled, here's a natural way to split the nine categories across five or six people:

1. Pair and Two Pair.
2. Three of a Kind and Four of a Kind.
3. Full House.
4. Straight and Straight Flush — watch out for the Ace-low straight (A-2-3-4-5).
5. Flush and High Card.
6. `compare_hands`, plus wiring `classify_hand` together once everyone else's category checks exist.

Start with Pair or High Card, since they're the simplest — that will exercise your shared hand representation before tackling the trickier cases. Leave the straights until your shared representation is solid, since they need to look at consecutive ranks rather than just counts of a single rank.

## How you'll be assessed

- **Correctness**: Your code should produce the correct output for all test cases.
- **Comprehension**: _Everybody_ should understand _all_ the code in the project.
- **Quality**: We'd like to see a data model that supports the functionality well, and sensible utilization of the Python features you learned throughout the bootcamp.

## How to run the tests

To run the tests, you can configure your IDE to run unittest tests in the "." directory. Alternatively, you can run the tests from the command line using the following command:

```bash
python -m unittest test_poker.py
```

## Further Reading

Check out [List of poker hands](https://en.wikipedia.org/wiki/List_of_poker_hands) on Wikipedia for the full ranking with examples.

Chek out [ How to Play Poker](https://www.youtube.com/watch?v=pSRGErzzIo4) video for a visual guide.
