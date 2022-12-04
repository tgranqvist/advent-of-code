from enum import StrEnum

class Move(StrEnum):
    Rock = "A",
    Paper = "B"
    Scissors = "C"

    def __str__(self):
        return self._name_

class Outcome(StrEnum):
    Lose = "X",
    Draw = "Y",
    Win = "Z"

    def __str__(self):
        return self._name_

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

LOSSES = {
    Move.Rock: [Move.Paper],
    Move.Paper: [Move.Scissors],
    Move.Scissors: [Move.Rock]
}

SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6

def parse_hand(hand: str) -> tuple[Move, Outcome]:
    move1, outcome = hand.split()
    return (Move(move1), Outcome(outcome))

def evaluate_round(opponent_move: Move, outcome: Outcome) -> int:
    if outcome == Outcome.Draw:
        return SCORE_DRAW + SCORES[opponent_move]
    
    if outcome == Outcome.Lose:
        player_move = VICTORIES[opponent_move][0]
        return SCORE_LOSS + SCORES[player_move]
    else:
        player_move = LOSSES[opponent_move][0]
        return SCORE_WIN + SCORES[player_move]

if __name__ == "__main__":
     with open("hands.txt", "r") as hands:
        total = 0
        for hand in hands:
            opponent_move, outcome = parse_hand(hand)
            score = evaluate_round(opponent_move, outcome)
            total += score
            print(f"Opponent played {opponent_move}, match needs to be {outcome}. I get {score}. Totaling {total}.")