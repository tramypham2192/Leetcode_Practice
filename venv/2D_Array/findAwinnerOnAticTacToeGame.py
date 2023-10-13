# SOLUTION 1: GOOD MEMORY BUT BAD RUNTIME
def tictactoe(moves):
    # need to use set instead of list because of we need unordered
    # need to use tuple instead of list inside set because set can not contain list
    # because list is mutable while set is immutable
    winning_cases = (# 3 winning cases for horizontal rows
                     {(0, 0), (0, 1), (0, 2)},
                     {(1, 0), (1, 1), (1, 2)},
                     {(2, 0), (2, 1), (2, 2)},
                     # 3 winning cases for vertical columns
                     {(0, 0), (1, 0), (2, 0)},
                     {(0, 1), (1, 1), (2, 1)},
                     {(0, 2), (1, 2), (2, 2)},
                     # 2 winning cases for 2 diagonals
                     {(0, 0), (1, 1), (2, 2)},
                     {(0, 2), (1, 1), (2, 0)},
    )
    # check if A wins
    movesOfA = set()
    movesOfB = set()
    for i in range(0, len(moves), 2):
        movesOfA.add(tuple(moves[i]))

    for case in winning_cases:
        if case.issubset(movesOfA):
            return "A"

    # check if B wins
    for j in range(1, len(moves), 2):
        movesOfB.add(tuple(moves[j]))
    for case in winning_cases:
        if case.issubset(movesOfB):
            return "B"

    # check if draw : all 9 spots are filled but neither A wins or B wins
    # check if still pending
    if movesOfA not in winning_cases and movesOfB not in winning_cases:
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"

# SOLUTION 2:


# print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
# print(tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
# print(tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(tictactoe([[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]))