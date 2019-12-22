from header import ATree
import os
import sys


# find the initial state and goal state
def read_input(file_path):
    initial_state = []
    goal_state = []
    fd = open(file_path, 'r')

    # find the initial state
    for i in range(4):
        line = fd.readline().strip('\n').split(' ')
        initial_state.append([])
        for j in line:
            initial_state[i].append(int(j))

    # skip empty line
    fd.readline()

    # find goal state
    for i in range(4):
        line = fd.readline().strip('\n').split(' ')
        goal_state.append([])
        for j in line:
            goal_state[i].append(int(j))

    return initial_state, goal_state


def find_goal_state(init_state, goal_state, output_file):
    atree = ATree(init_state, goal_state)
    atree.search_goal()
    print('Solving...')

    # create a new output file
    if os.path.exists(output_file):
        os.remove(output_file)
    fd = open(output_file, 'a')

    # write initial state
    for i in range(4):
        st = str(init_state[i][0]) + ' ' + str(init_state[i][1]) + ' ' + str(init_state[i][2]) + ' ' + str(
            init_state[i][3]) + '\n'
        fd.write(st)
    fd.write('\n')

    # write goal state
    for i in range(4):
        st = str(goal_state[i][0]) + ' ' + str(goal_state[i][1]) + ' ' + str(goal_state[i][2]) + ' ' + str(
            goal_state[i][3]) + '\n'
        fd.write(st)
    fd.write('\n')

    # write depth
    fd.write(str(atree.depth))
    fd.write('\n')

    # write number of nodes
    fd.write(str(atree.nodes_num))
    fd.write('\n')

    # write actions
    st = ''
    for action in atree.actions_to_goal:
        st += action + ' '
    st += '\n'
    fd.write(st)

    # write costs
    st = ''
    for cost in atree.cost_of_node:
        st += str(cost) + ' '
    fd.write(st)
    print('Finished.')


def main():
    # get input file
    input_file = sys.argv[1]

    # name output file
    output_file = 'Output'+input_file[5]+'.txt'

    initial_stat, goal_state = read_input(input_file)
    find_goal_state(initial_stat, goal_state, output_file)


if __name__ == "__main__":
    main()
