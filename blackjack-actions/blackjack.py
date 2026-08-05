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
        "dealer": dealer_upcard,
        "can_double": can_double
    }


def generate_actions(state):
    actions = []

    # Player can always hit or stand
    actions.append("hit")
    actions.append("stand")

    # Player can only double with two cards
    if state["can_double"] == True:
        if len(state["hand"]) == 2:
            actions.append("double")

    return actions


def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")
