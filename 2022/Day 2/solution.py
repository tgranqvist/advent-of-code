from enum import StrEnum

class Move(StrEnum):
    Rock = "A",
    Paper = "B"
    Scissors = "C"

XLATE = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

SCORES = {
    Move.Rock: 1,
    Move.Paper: 2,
    Move.Scissors: 3
}

VICTORIES = {
    Move.Rock: [Move.Scissors],
    Move.Paper: [Move.Rock],
    Move.Scissors: [Move.Paper]
}

SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6

def parse_hand(hand):
    move1, move2 = hand.split()
    move2 = XLATE[move2]

    return (Move(move1), Move(move2))

def evaluate_round(opponent: Move, player: Move) -> int:
    if opponent == player:
        return SCORE_DRAW + SCORES[player]
    
    defeats = VICTORIES[player]
    if opponent in defeats:
        return SCORE_WIN + SCORES[player]
    else:
        return SCORE_LOSS + SCORES[player]

if __name__ == "__main__":
     with open("hands.txt", "r") as hands:
        total = 0
        for hand in hands:
            opponent, me = parse_hand(hand)
            score = evaluate_round(opponent, me)
            total += score
            print(f"Opponent played {opponent}, I played {me} for {score}. Totaling {total}")