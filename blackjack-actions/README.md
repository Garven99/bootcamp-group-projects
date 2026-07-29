# Project - Blackjack Actions

In this project, you'll implement the decision rules for a single player's turn in Blackjack (21). You'll be given a hand, the dealer's up card, and whether this is your first decision this turn, and asked to work out which actions are currently legal, and what happens when you take one.

## Project Overview

Blackjack is played with a standard 52-card deck. Card ranks 2-10 are worth their face value, J/Q/K are worth 10, and Aces are worth 11 or 1, whichever keeps your hand at 21 or under (a hand containing an Ace counted as 11 is called "soft"). The goal is to get your hand's total as close to 21 as possible without going over ("busting"), beating the dealer's hand.

At each decision point in your turn, you may:

- **Hit**: take another card.
- **Stand**: take no more cards, ending your turn.
- **Double Down**: double your bet, take exactly one more card, and stand — only allowed as your very first decision, before you've hit.
- **Split**: if your first two cards share the same rank (e.g. two 8s), split them into two separate hands, each starting with one of the cards — only allowed as your first decision.
- **Surrender**: forfeit half your bet and end your turn immediately, without taking any more cards — only allowed as your first decision.
- **Insurance**: a side bet you may take only when the dealer's up card is an Ace, and only as your first decision. It doesn't end your turn or change your hand.

For this project, you need to implement handling for all six of these actions.

We'd like a convenient text notation for describing a decision point, similar in spirit to chess's FEN. A card is written as its rank: `2`-`10`, `J`, `Q`, `K`, `A`. A decision point is written as three fields separated by `|`:

```
10,6 | 9 | first
```

This means: your hand is a 10 and a 6, the dealer shows a 9, and this is your first decision this turn (you haven't hit yet). Once you've hit at least once, the last field becomes `later`, which rules out Double Down, Split, Surrender, and Insurance.

`hand_value` and `RANK_VALUES` are provided for you in `blackjack.py` — you don't need to re-derive how soft Aces work, just use them.

## Project Requirements

- Implement a function that parses a decision-point string into a convenient representation.
- Implement a function that generates the legal actions for a decision point.
- Implement a function that applies a chosen action, returning the resulting hand (or, for Split, the two resulting hands).

You do not need to implement the dealer's turn, betting/bankroll tracking, re-splitting a split hand, doubling after a split, or determining a winner. Focus on: given one hand and the current decision point, what can the player do, and what does their hand look like afterwards?

## Notes on teamwork

Your team needs to decide how a decision point and a hand will be represented in Python before splitting up the work — this is the core decision everybody depends on. Explore this with your team first, writing some test code together. It would be a mistake to split up the work before agreeing on the data model.

Once that's settled, split up the six actions above, one per person. Start with Hit and Stand together, since they're legal in every situation and will exercise your shared data model without any of the "only as your first decision" conditions the other four share. Save Split for last, since it's the only action that produces two hands instead of one, and that's worth agreeing on as a team rather than improvising alone.

## How you'll be assessed

- **Correctness**: Your code should produce the correct output for all test cases.
- **Comprehension**: _Everybody_ should understand _all_ the code in the project.
- **Quality**: We'd like to see a data model that supports the functionality well, and sensible utilization of the Python features you learned throughout the bootcamp.

## How to run the tests

To run the tests, you can configure your IDE to run unittest tests in the "." directory. Alternatively, you can run the tests from the command line using the following command:

```bash
python -m unittest test_blackjack.py
```

## Youtube Video Explaining Blackjack
Check out [How to Play Blackjack: Learn from an Expert](https://www.youtube.com/watch?v=UXmbwvr3aKk).
