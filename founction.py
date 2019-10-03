#Import library
import sys
import time
import math
import random




def ran(domain): # generate two numbers to swap 
    num = []
    first = random.randint(1,domain)
    num.append(first)
    second = random.randint(1,domain)
    ok=0
    if domain >1:
        while(ok==0):
            if second != first:
                num.append(second)
                ok=1
            else:
                second = random.randint(1,domain)
                ok=0   
    return num


def init(num): # generate init random city sequence
    seq = []
    while len(seq) < num:
        temp = random.randint(1,num)
        if temp not in seq: 
            seq.append(temp)
    
    return seq


def transform(seq): # swap two city location
    new = seq[:]
    index = ran(len(seq))
                
    t = new[index[0]-1]
    new[index[0]-1] = new[index[1]-1]
    new[index[1]-1] = t

    return new


def distance(axis): # caculate the two cities' distance
    return  math.sqrt(pow(axis[0],2)+pow(axis[1],2))


def TotalDistance(seq,dic): # sum the all seq's distance
    dist = 0
    for i in range(len(seq)):
        dx = dic[seq[i]][0]-dic[seq[(i+1)%len(seq)]][0]
        dy = dic[seq[i]][1]-dic[seq[(i+1)%len(seq)]][1]
        d =  [dx,dy]
        dist += distance(d)
    return dist


def HC_determine(temp,min_seq,dic): # record the min_seq & min_distance 
    
    if TotalDistance(temp,dic) < TotalDistance(min_seq,dic):
        min_seq = temp[:]
    return min_seq,TotalDistance(temp,dic)


def SA_determine(neighbors,seq_current,dic,temperature,seq_best): #check if it is a better seq or decide seq_ccurrent go new spot or not with a random posibility
    index = random.randint(0,len(neighbors)-1)
    value = TotalDistance(neighbors[index],dic) - TotalDistance(seq_current,dic)
    if value <= 0:
        seq_current = neighbors[index]
        seq_best = seq_current[:]
    else:
        r = random.random()
        if math.exp((-10)*value/temperature) >= r:
            seq_current = neighbors[index]

    return seq_current,seq_best


def neighbors_generator(seq,num): #choose random neughbor
    neighbor=[]
    for i in range(num):
        temp = transform(seq)
        if temp not in neighbor:
            neighbor.append(temp)
    return neighbor


def readfile(dic): # readfile eil51.txt
    with open('eil51.txt') as f:
        r = f.read()
        read_line = r.split('\n')               
        for i in range(len(read_line)):         
            read_element = read_line[i].split()
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        f.close()
