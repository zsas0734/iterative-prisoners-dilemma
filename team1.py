from sklearn.svm import SVC
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
# Ver. 10/11/2018

team_name = 'Team1'
strategy_name = 'Predict Movement'
strategy_description = 'Base on the history of the enemy, predict what would the enemy decide, then decide base on the prediction and scores.'

input_data = [['c','c','c'],['b','b','b'],['c','b','c'],['b','c','b']]
output_data = ['c','b','c','b']


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    output_data.append(their_history[-1])
    
    strategy = SVC()
    strategy.fit = (input_data, output_data)
    
    enemy_choice = strategy.predict([[their_history[-3], their_history[-2], their_history[-1]]])[0]
    
    if enemy_choice == 'c' and int(their_score) >= int(my_score) :
        return 'b'
    elif enemy_choice == 'b' and int(their_score) >= int(my_score):
        return 'b'
    elif enemy_choice == 'c' and int(their_score) < int(my_score):
        return 'c'
    elif enemy_choice == 'b' and int(their_score) < int(my_score) :
        return 'b'
    else:
        return 'c'

    if len(their_history) > 3:
        input_data.append([their_history[-3],their_history[-2],their_history[-1]]
    
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
