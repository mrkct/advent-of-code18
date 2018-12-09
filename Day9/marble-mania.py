# NOTE: This one doesn't load the input from the file. It's not worth it

def add_clockwise(marbles, current_marble, to_add):
    if len(marbles) == 1:
        marbles.append(to_add)
        return 1
    else:
        new_current_marble = (current_marble + 2)
        if new_current_marble == len(marbles):
            marbles.append(to_add)
        else:
            new_current_marble = new_current_marble % len(marbles)
            marbles.insert( new_current_marble, to_add )
        return new_current_marble

def remove_counterclockwise(marbles, current_marble, step):
    to_remove = (current_marble-step) % len(marbles)
    del marbles[to_remove]

    return to_remove % len(marbles)

# Insert the input here
players = 464
marbles_max = 71730

scores = [0 for _ in range(players)]
marbles = [0]
current_marble = 0
current_player = 0

for i in range(1, marbles_max):
    if i % 23 != 0:
        current_marble = add_clockwise(marbles, current_marble, i)
    else:
        scores[current_player] += i
        scores[current_player] += marbles[(current_marble-7) % len(marbles)]
        current_marble = remove_counterclockwise(marbles, current_marble, 7)
    current_player = (current_player + 1) % players

print(max(scores))