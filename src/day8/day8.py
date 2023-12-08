from queue import Queue
from collections import  defaultdict
from functools import reduce
import math

def parse_input(filename) :
    with open(filename,'r') as f :
        data = [line.strip() for line in f if line.strip() != '' ]
        dir = data[0]
        data = data[1:]
        data = [(d.split('=')[0].strip(),d.split('=')[1].strip()) for d in data]
        data = [ (d[0],d[1].split(',')[0].replace('(','').strip(),d[1].split(',')[1].replace(')','').strip() ) for d in data]
        return dir,data

def get_neighbour(data) :
    nb = defaultdict(list)
    for d in data :
        nb[d[0]].append(d[1])
        nb[d[0]].append(d[2])
    return nb

def get_steps_1(data,dir) :
    nb = get_neighbour(data)
    cur = 'AAA'
    n_steps = 0
    while cur != 'ZZZ' :
        for d in dir :
            if d == 'L' :
                cur = nb[cur][0]
            else :
                cur = nb[cur][1]
            n_steps += 1
    return n_steps

def get_dest(node,dir,nb) :
    dest = node
    for d in dir :
        if d == 'L':
            dest=nb[dest][0]
        else :
            dest=nb[dest][1]
    return dest

def get_lcm(numbers) :
    return reduce(math.lcm, numbers)
def get_steps_2(data,dir) :
    nb = get_neighbour(data)
    start_nodes = [node for node in nb.keys() if node[-1] == 'A']
    end_nodes = [node for node in nb.keys() if node[-1] == 'Z']
    save_steps = {}
    for node in nb.keys() :
        save_steps[node] = get_dest(node,dir,nb)
    print('Source node are ',start_nodes)
    cycles = []
    # while not all(cur_node in end_nodes for cur_node in cur_nodes ) :
    #         cur_nodes = [save_steps[cur_node] for cur_node in cur_nodes]
    #         print(cur_nodes)
    #         n_steps += 1
    for node in start_nodes :
        n_cycles = 0
        while not node in end_nodes :
            node = save_steps[node]
            n_cycles += 1
        cycles.append(n_cycles)
        print('Cycle',cycles)

    lcm = int(get_lcm(cycles))
    return lcm*len(dir)


def get_shortest_path(data) :
    nb = get_neighbour(data)
    print(nb)
    source = 'AAA'
    dest = 'ZZZ'
    q = Queue()
    q.put((source,0))
    while not q.empty() :
        node = q.get()
        if node[0] == dest :
            return node[1]
        q.put( (nb[node[0]][0], node[1] + 1))
        q.put( (nb[node[0]][1], node[1] + 1) )


dir,data = parse_input('day8.txt')
ans = get_steps_2(data,dir)
print(ans)