# A dictionary for a deck of cards
RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11,
}

# Sum of the number of the cards each player has
def hand_value(cards):
    total = sum(RANK_VALUES[card] for card in cards)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# Displays the game
def parse_state(text):
    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")]
    hand = [rank.strip() for rank in hand_str.split(",")]

    return {
        "hand": hand,
        "dealer_upcard": dealer_upcard,
        "total": hand_value(hand),
        "can_double": flag == "first",
        "can_surrender": flag == "first",
        "busted": False,
    }

def generate_actions(state):
    actions = []

    # Always legal
    actions.append("hit")
    actions.append("stand")

    # Double and surrender only on first decision with 2 cards
    if state["can_double"] and len(state["hand"]) == 2:
        actions.append("double")
        actions.append("surrender")

    # Split requires matching ranks and first decision
    if len(state["hand"]) == 2:
        if state["hand"][0] == state["hand"][1]:
            actions.append("split")

    # Insurance only against dealer Ace
    if state["dealer_upcard"] == "A":
        actions.append("insurance")

    return actions

def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")
