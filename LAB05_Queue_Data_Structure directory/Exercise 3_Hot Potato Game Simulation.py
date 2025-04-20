import random
from collections import deque

def hot_potato_game(players, max_passes):
    queue = deque(players)

    while len(queue) > 1:
        passes = random.randint(1, max_passes)
        print(f"\nRound with {passes} passes")

        for _ in range(passes):
            player = queue.popleft()
            queue.append(player)
            print(f"Hot potato passed to {player}")

        eliminated = queue.popleft()
        print(f"💥 {eliminated} is eliminated!")

    winner = queue[0]
    print(f"\n🏆 The winner is: {winner}")
    return winner

players = ["Alice", "Bob", "Charlie"]
max_passes = 3
hot_potato_game(players, max_passes)

players = ["Tom", "Jerry", "Spike", "Tyke"]
max_passes = 6
hot_potato_game(players, max_passes)

players = ["Anna", "Ben"]
max_passes = 2
hot_potato_game(players, max_passes)