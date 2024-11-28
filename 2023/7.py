
import re
from collections import defaultdict

with open("7.txt", "r") as f:
        lines = f.readlines()


def grt_hand_type(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts and 2 in counts:
        return 4
    if 3 in counts and 2 not in counts:
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

    
def get_inputs():

    letters_rank = {"A" : "E", "K" : "D", "Q" : "C", "J" : "B", "T" : "A"}
    all_hands = []
    for line in lines:
        line = line.replace("\n", "")
        hand, bid = line.split()
        hands_type = grt_hand_type(hand)
        hand = "".join(letters_rank[card] if card in letters_rank else card for card in hand )
        all_hands.append((hand, hands_type, int(bid)))

    return all_hands


def part_one():
    all_hands = get_inputs()
    all_hands.sort(key=lambda x: x[1])

    all_hands_dict = defaultdict(list)
    for hand in all_hands:
        all_hands_dict[hand[1]].append(hand)

    sorted_all_hands = []
    for v in all_hands_dict.values():
        sorted_all_hands += sorted(v, key=lambda x: x[0])

    winning = 0
    for rank, card in enumerate(sorted_all_hands, 1):
        winning += rank * card[2]

    print(winning)

def grt_hand_type_j(hand):

    card_list = list(set(hand))
    if len(card_list) == 1:
        return 6
    card_list.remove("J")
    card_scores = []
    for card in card_list:
        temp_hand = hand
        card_scores.append(grt_hand_type(temp_hand.replace("J", card)))

    return max(card_scores)

def get_input2():
    letters_rank = {"A" : "E", "K" : "D", "Q" : "C", "J" : "1", "T" : "A"}
    all_hands = []
    for line in lines:
        line = line.replace("\n", "")
        hand, bid = line.split()
        if "J" in hand:
            hands_type = grt_hand_type_j(hand)
        else:
            hands_type = grt_hand_type(hand)

        hand = "".join(letters_rank[card] if card in letters_rank else card for card in hand )
        all_hands.append((hand, hands_type, int(bid)))

    return all_hands


def part_two():
    all_hands = get_input2()
    all_hands.sort(key=lambda x: x[1])

    all_hands_dict = defaultdict(list)
    for hand in all_hands:
        all_hands_dict[hand[1]].append(hand)

    sorted_all_hands = []
    for v in all_hands_dict.values():
        sorted_all_hands += sorted(v, key=lambda x: x[0])

    winning = 0
    for rank, card in enumerate(sorted_all_hands, 1):
        winning += rank * card[2]

    print(winning)



if __name__ == "__main__":
    
    part_one()
    part_two()