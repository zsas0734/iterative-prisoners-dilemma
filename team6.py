import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Exposed' The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'If neccessary''The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'

retaliation = ['b', 'b', 'c', 'c', 'b']
always_betray = ['b', 'b','b','b','b']
always_collude = ['c', 'c', 'c', 'c', 'c']
og_pattern = ['b','b','c','c','b']
strategies = [retaliation, always_betray, always_collude, og_pattern]
def move(my_history, their_history):
    ''' Arguments accepted: my_history, their_history are strings.
    are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if my_history[0]:
        return 'b'
    if my_history[1]:
        return 'b'
    if my_history[2]:
        return 'c'
    if my_history[3]:
        return 'c'
    if my_history[4]:
        return 'b'
    if their_history == ['c', 'b', 'b', 'c', 'c']:
        return retaliation
    if their_history == ['c', 'c', 'c', 'c', 'c']:
        return always_betray
    if their_history == ['b', 'b', 'b', 'b', 'b']:
        return always_collude
    else:
        random.choice(strategies)
        
        

        
    

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'     