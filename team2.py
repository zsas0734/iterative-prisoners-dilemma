####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The High Ground' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
        
def reaction_time(their_history):
    alwaysCollude = True
    if "b" in their_history:
        alwaysCollude = False
        return their_history[-1]
    while alwaysCollude == True:
        return 'c'

def passive_agressive(my_score, my_history):
    start_collude = True
    if start_collude == True:
        return 'c'
    if len(my_score) == 50:
        start_collude = False
        return reaction_time
    elif my_score >= -1000:
        start_collude = False
        return reaction_time
        
def tasteofmedicine(my_history, their_history):
    start_betray = True
    if start_betray == True:
        return 'b'
    if len(my_history) == 50:
        for a in their_history:
            return a

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    return reaction_time