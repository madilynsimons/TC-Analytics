#!/usr/bin/python

f = open("in.txt", "r")

for line in f.read():
    print(line)


f.close()

