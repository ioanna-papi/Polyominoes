import sys
import pprint
arguments = len(sys.argv) -1
if (arguments == 1):
    num = int(sys.argv[1])
elif (arguments == 2):
    num = int(sys.argv[2])
else:
    num = 0
key = []
graph = dict()
def Condition(x, y):
    if(y == 0 and x >= 0) or (y > 0 and x >= 0 and (x + y) < num) or (y > 0 and x < 0 and (y - x) < num ):
        return 'yes'
    else:
        return 'no'

for x in range((2-num), num):
    for y in range(0, num):
        if Condition(x, y) == 'yes':
            key.append((x,y))

for k in key:
    graph[tuple(k)] = []

for x in range((2-num), num):
    for y in range(0, num):
        if Condition(x, y) == 'yes':
            if (Condition(x+1, y) == 'yes' and x+1 < num):
                graph[(x,y)].append((x+1, y))
            if (Condition(x, y+1)  == 'yes' and y+1 < num):
                graph[(x,y)].append((x, y+1))
            if Condition(x-1, y)  == 'yes':
                graph[(x,y)].append((x-1, y))
            if Condition(x, y-1) == 'yes':
                graph[(x,y)].append((x, y-1))

def Neighbors(ls, v, u):
    flag = 'not'
    for l in ls:
        if l != u:
            if v in graph[l]:
                flag = 'they are'
                break
    return flag

class Counter:
    def __init__(self, counter):
        self.counter = counter
    def add_one(self, c):
        counter = c + 1
        self.counter = counter
    def counter_value(self):
        return self.counter

def countPolyominoes(graph,untried,n,p,c):
    while len(untried) != 0:
        u = untried.pop()
        p.append(u)
        if len(p) == n:
            c.add_one(c.counter_value())
        else:
            new_neighbors = set()
            for v in graph[u]:
                if((v not in untried) and (v not in p) and (Neighbors(p, v, u) == 'not')):
                    new_neighbors.add(v)
            new_untried = untried.union(new_neighbors)
            countPolyominoes(graph,new_untried,n,p,c)
        p.remove(u)
    return c.counter_value()

unt = {(0,0)}
p1 = []
c = Counter(0)
if arguments == 2:
    pprint.pprint(graph)
print(countPolyominoes(graph,unt,num,p1,c))

