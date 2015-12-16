from collections import defaultdict, Counter

N = int(input())#read number of tuples
mapGroupAge = defaultdict(Counter)#a dict of counters to count 
                                  #the repetitions by group

for _ in range(N):
    # read tuples (from standard input in this example)
    group,name,age,color = input().split()
    #build the map (dict) indexed by the groups i.e. a key is a pair (group,name)
    mapGroupAge[(group,name)][(age,color)] += 1

for (group,name), counter in mapGroupAge.items():
    # if all ages and colors for the same group are the same
    if(len(counter)==1):
        age,color = list(counter.keys())[0]
        # print all the repetitions
        for _ in range(counter[(age,color)]):
            print(group, name, age,color)


