# from model import Hunter
import random

hunter_location_a = 'J17'
hunter_location_b = 'K17'
agent_previous_location = 'N1'
mission_objective_a = [[5, 10], [5, 11], [5, 12], [6, 10], [6, 12], [7, 10], [7, 11], [7, 12]]
mission_objective_b = [[6, 28], [6, 29], [6, 30], [7, 28], [7, 30], [8, 28], [8, 29], [8, 30]]
mission_objective_c = [[20, 24], [20, 25], [20, 26], [21, 24], [21, 26], [22, 24], [22, 25], [22, 26]]
mission_objective_d = [[21, 15], [21, 16], [21, 17], [22, 15], [22, 17], [23, 15], [23, 16], [23, 17]]
mission_objectives = [mission_objective_a, mission_objective_b, mission_objective_c, mission_objective_d]
streets = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7], [10, 7], [11, 7], [12, 7], [13, 7], [14, 7], [15, 7],
    [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8],
    [14, 12], [15, 12], [16, 12], [17, 12], [18, 12], [19, 12], [20, 12],[21, 12], [22, 12], [23, 12],
    [14, 13], [15, 13], [16, 13], [17, 13], [18, 13], [19, 13], [20, 13],[21, 13], [22, 13], [23, 13],
    [1, 15], [2, 15], [3, 15], [4, 15], [5, 15], [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15], [15, 15],
    [1, 16], [2, 16], [3, 16], [4, 16], [5, 16], [6, 16], [7, 16], [8, 16], [9, 16], [10, 16], [11, 16], [12, 16], [13, 16], [14, 16], [15, 16],
    [10, 21], [11, 21], [12, 21], [13, 21], [14, 21], [15, 21], [16, 21], [17, 21], [18, 21], [19, 21], [20, 21], [21, 21], [22, 21], [23, 21],
    [10, 22], [11, 22], [12, 22], [13, 22], [14, 22], [15, 22], [16, 22], [17, 22], [18, 22], [19, 22], [20, 22], [21, 22], [22, 22], [23, 22],
    [1, 23], [2, 23], [3, 23], [4, 23], [5, 23], [6, 23], [7, 23], [8, 23], [9, 23], [10, 23], [11, 23],
    [1, 24], [2, 24], [3, 24], [4, 24], [5, 24], [6, 24], [7, 24], [8, 24], [9, 24], [10, 24], [11, 24],
    [14, 1], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 9], [14, 10], [14, 11], [14, 14],
    [15, 1], [15, 2], [15, 3], [15, 4], [15, 5], [15, 6], [15, 9], [15, 10], [15, 11], [15, 14],
    [10, 17], [10, 18], [10, 19], [10, 20], [10, 25], [10, 26], [10, 27], [10, 28], [10, 29], [10, 30], [10, 31], [10, 32],
    [11, 17], [11, 18], [11, 19], [11, 20], [11, 25], [11, 26], [11, 27], [11, 28], [11, 29], [11, 30], [11, 31], [11, 32] ]

obstruction = [
    [1, 2], [1, 4], [1, 9], [1, 14], [1, 17], [1, 21], [1, 22], [1, 27], [1, 28],
    [2, 6], [2, 11], [2, 12], [2, 19], [2, 25], [2, 30], [2, 32],
    [3, 1], [3, 3], [3, 4], [3, 6], [3, 9], [3, 14], [3, 17], [3, 21], [3, 22], [3, 25], [3, 26], [3, 28], [3, 32],
    [4, 3], [4, 9], [4, 10], [4, 12], [4, 19], [4, 30],
    [5, 1], [5, 5], [5, 6], [5, 14], [5, 17], [5, 21], [5, 22], [5, 25], [5, 27], [5, 29], [5, 30], [5, 32],
    [6, 3], [6, 9], [6, 11], [6, 13], [6, 14], [6, 19], [6, 22], [6, 25],
    [7, 1], [7, 5], [7, 6], [7, 14], [7, 17], [7, 19], [7, 20], [7, 27], [7, 29], [7, 31], [7, 32],
    [8, 3], [8, 6], [8, 9], [8, 10], [8, 12], [8, 22], [8, 25],
    [9, 1], [9, 3], [9, 4], [9, 9], [9, 14], [9, 17], [9, 18], [9, 20], [9, 22], [9, 25], [9, 27], [9, 28], [9, 30], [9, 32],
    [10, 6], [10, 11], [10, 12], [10, 14],
    [11, 1], [11, 2], [11, 4], [11, 9], [11, 11], [11, 12],
    [12, 6], [12, 14], [12, 17], [12, 18], [12, 20], [12, 23], [12, 24], [12, 26], [12, 27], [12, 29], [12, 30], [12, 32],
    [13, 2], [13, 3], [13, 5], [13, 6], [13, 9], [13, 11], [13, 13], [13, 14], [13, 27],
    [14, 17], [14, 19], [14, 20], [14, 23], [14, 25], [14, 29], [14, 31],
    [15, 20], [15, 25], [15, 26], [15, 28], [15, 29],
    [16, 2], [16, 3], [16, 5], [16, 7], [16, 9], [16, 11], [16, 14], [16, 16], [16, 18], [16, 23], [16, 31], [16, 32],
    [17, 2], [17, 11], [17, 14], [17, 16], [17, 20], [17, 25], [17, 27], [17, 29],
    [18, 4], [18, 6], [18, 7], [18, 9], [18, 18], [18, 23], [18, 31],
    [19, 1], [19, 2], [19, 6], [19, 11], [19, 14], [19, 15], [19, 16], [19, 20], [19, 23], [19, 24], [19, 26], [19, 27], [19, 29],
    [20, 1], [20, 4], [20, 8], [20, 10], [20, 11], [20, 16], [20, 18], [20, 27], [20, 29], [20, 31], [20, 32],
    [21, 1], [21, 2], [21, 6], [21, 8], [21, 14], [21, 20], [21, 23], [21, 25],
    [22, 1], [22, 2], [22, 4], [22, 6], [22, 10], [22, 11], [22, 16], [22, 18], [22, 23], [22, 27], [22, 28], [22, 30], [22, 32],
    [23, 1], [23, 4], [23, 8], [23, 14], [23, 20], [23, 25],
]



def top_priority(vec1, vec2):
  vec2 = vec1
  while vec2 not in streets:
    vec2[1] -= 1

  vec2 = chr(vec2[0] + ord('A') - 1, ) + str(vec2[1])
  return vec2

def cover_ground(vec1, vec2):
    x = vec1[0] - vec2[0]
    y = vec1[1] - vec2[1]

    if x > 0:
         x_dir = 1
    elif x < 0:
         x_dir = -1
    else:
         x_dir = 0

    if y > 0:
         y_dir = 1
    elif y < 0:
         y_dir = -1
    else:
         y_dir = 0

    for _ in range(4):
        next_x = vec2[0] + x_dir
        next_y = vec2[1] + y_dir
        if [next_x, next_y] == vec1:
            next_y += 1
            break

        vec2 = [next_x, next_y]

    while vec2 in obstruction:
        if vec1[0] > vec2[0]:
            vec2[0] += 1
        else:
            vec2[0] -= 1

    vec2 = chr(vec2[0] + ord('A') - 1, ) + str(vec2[1])
    return vec2


def false_lead1(vec1, vec2):
    x = vec1[0] - vec2[0]
    y = vec1[1] - vec2[1]

    if x < 0:
         x_dir = 1
    elif x > 0:
         x_dir = -1
    else:
         x_dir = 0

    if y > 0:
         y_dir = 1
    elif y < 0:
         y_dir = -1
    else:
         y_dir = 0

    for _ in range(4):
        next_x = vec2[0] + x_dir
        next_y = vec2[1] + y_dir
        if [next_x, next_y] == vec1:
            break

        vec2 = [next_x, next_y]

    while vec2 in obstruction:
        if vec1[0] > vec2[0]:
            vec2[0] += 1
        else:
            vec2[0] -= 1

    vec2 = chr(vec2[0] + ord('A') - 1, ) + str(vec2[1])
    return vec2

def false_lead2(vec1, vec2):
    x = vec1[0] - vec2[0]
    y = vec1[1] - vec2[1]

    if x > 0:
         x_dir = 1
    elif x < 0:
         x_dir = -1
    else:
         x_dir = 0

    if y < 0:
         y_dir = 1
    elif y > 0:
         y_dir = -1
    else:
         y_dir = 0

    for _ in range(4):
        next_x = vec2[0] + x_dir
        next_y = vec2[1] + y_dir
        if [next_x, next_y] == vec1:
            break

        vec2 = [next_x, next_y]

    while vec2 in obstruction:
        if vec1[0] > vec2[0]:
            vec2[0] += 1
        else:
            vec2[0] -= 1

    vec2 = chr(vec2[0] + ord('A') - 1, ) + str(vec2[1])
    return vec2

def search1(vec1, vec2):
    choice = random.randint(1, 10)
    if choice <= 5:
        vec2 = cover_ground(vec1, vec2)
        return vec2
    elif choice <= 7:
        vec2 = false_lead1(vec1, vec2)
        return vec2
    else:
        vec2 = false_lead2(vec1, vec2)
        return vec2

# def search2(vec1, vec2):
#     choice = random.randint(1, 10)
#     if choice <= 4:
#         vec2 = cover_ground(vec1, vec2)
#         return vec2
#     elif choice <= 7:
#         vec2 = false_lead1(vec1, vec2)
#         return vec2
#     else:
#         vec2 = false_lead2(vec1, vec2)
#         return vec2



def opponent(space, vision, mission):
    global hunter_location_a
    global hunter_location_b
    agent = [ord(space[0]) - ord('A') +1, int(space[1:])] #create agent vector
    hunter_location_b = hunter_B(agent, vision, mission)
    hunter_location_a = hunter_A(agent, vision, mission)
    print(hunter_location_a, hunter_location_b)
    return [hunter_location_a, hunter_location_b]


def hunter_A(agent, vision, mission):
    global hunter_location_a
    hunter_vector_a = [ord(hunter_location_a[0]) - ord('A') +1, int(hunter_location_a[1:])]

    if mission or vision:
        hunter_location_a = cover_ground(agent, hunter_vector_a)
        return hunter_location_a
    else:
        hunter_location_a = search1(agent, hunter_vector_a)
        return hunter_location_a

def hunter_B(agent, vision, mission):
    global hunter_location_b
    hunter_vector_b = [ord(hunter_location_b[0]) - ord('A') +1, int(hunter_location_b[1:])] #create hunter_B vector

    if mission or vision:
        if hunter_vector_b in streets:
            hunter_location_b = top_priority(agent, hunter_vector_b)
            return hunter_location_b
        else:
             hunter_location_b = cover_ground(agent, hunter_vector_b)
             return hunter_location_b
    else:
        hunter_location_b = search1(agent, hunter_vector_b)
        return hunter_location_b
