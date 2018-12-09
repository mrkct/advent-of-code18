# NOTE: This one doesn't load the input from the file. It's not worth it

'''
    The previous part was bottlenecked by the list.insert
    function. Internally, python uses an array to represent
    lists. This part includes a very simple implementation of
    a circular double-linked list
'''

'''
    Attaches a new node for to_add just after
    the element pointed by linked_list. Returns
    the new node
'''
def llist_appendnext(linked_list, to_add):
    new = dict(
        next=linked_list['next'],
        prev=linked_list,
        value=to_add
    )
    linked_list['next'] = new
    new['next']['prev'] = new
    
    return new

'''
    Moves 'step' steps forward or backward from
    the node pointed by linked_list. Returns the
    reached node
'''
def llist_move(linked_list, step):
    for _ in range(abs(step)):
        if step < 0:
            linked_list = linked_list['prev']
        else:
            linked_list = linked_list['next']
    
    return linked_list

'''
    Removes the linked_list node and returns the node
    just after the removed one. This doesnt work if
    there is only 1 node, but it doesnt matter for this
    part
'''
def llist_remove(linked_list):
    prev = linked_list['prev']
    next = linked_list['next']
    prev['next'] = next
    next['prev'] = prev

    return next

def add_clockwise(current_marble, to_add):
    current_marble = llist_move(current_marble, 1)
    return llist_appendnext(current_marble, to_add)

def remove_counterclockwise(current_marble, step):
    current_marble = llist_move(current_marble, step)
    to_remove = (current_marble-step) % len(marbles)
    del marbles[to_remove]

    return to_remove % len(marbles)

# Insert the input here
players = 464
marbles_max = 71730 * 100

scores = [0 for _ in range(players)]
current_marble = dict(
    next=None,
    prev=None,
    value=0
)
current_marble['next'] = current_marble['prev'] = current_marble
current_player = 0

for i in range(1, marbles_max):
    if i % 23 != 0:
        current_marble = llist_move(current_marble, 1)
        current_marble = llist_appendnext(current_marble, i)
    else:
        scores[current_player] += i
        current_marble = llist_move(current_marble, -7)
        scores[current_player] += current_marble['value']
        current_marble = llist_remove(current_marble)
    current_player = (current_player + 1) % players

print(max(scores))