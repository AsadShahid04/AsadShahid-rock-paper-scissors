# the strategy is similar to abbey, but we look backs harder than her.
# she only look back 2 steps, find most frequently pattern of all 2 moves,
#
# Other strategies:
#
# - quincy repeat 5 moves
# - kris always counter our last moves, hence, once we establed a patterns, he
# is not a problem
# - mrugresh look for our top pick in last 10 moves, hence, similar to kris,
# once we establed a pattern, we're in control.
steps = {}

def player(prev_play, opponent_history=[]):
  global steps

  n = 6

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "P" # default, until statistic kicks in

  if len(opponent_history)>n:
    input = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in steps.keys():
      steps["".join(opponent_history[-(n+1):])]+=1
    else:
      steps["".join(opponent_history[-(n+1):])]=1

    possible = [input+"R", input+"P", input+"S"]

    for i in possible:
      if not i in steps.keys():
        steps[i] = 0

    predict = max(possible, key=lambda key: steps[key])

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"


  return guess

# # The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess
