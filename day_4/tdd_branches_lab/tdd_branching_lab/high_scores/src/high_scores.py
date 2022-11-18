def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)
 

def personal_top_three(scores):
    scores.sort()
    return scores[-3::]

def high_to_low(scores):
    numbers = sorted(scores)
    return numbers[::-1]

