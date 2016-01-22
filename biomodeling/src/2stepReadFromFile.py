#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "run as main program"
def readDataFromFile(filename):
    f = open(filename, 'r')
    goon=True
    count=0
    lines=f.readline()
    columns=f.readline()
    print lines
    print columns
    i=0
    for line in f:
        print i
        i+=1
        cols=line.rstrip().split("\t")
        print cols[0]
    return

#this is the main program
filename= "output_2016-01-22_01_15_36.dat"
readDataFromFile(filename)