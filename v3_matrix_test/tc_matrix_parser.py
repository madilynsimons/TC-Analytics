#!/usr/bin/python

in_file = open("in.txt", "r")
out_file = open("out.csv", "w")

out_file.write("x,y\n")

for line in in_file:
    words = line.split()

    if words[0] == "D/stencil_location_y:":
        y = float(words[1])
        out_file.write(",%f\n" % y)
    elif words[0] == "D/stencil_location_x:":
        x = float(words[1])
        out_file.write("%f" % x)

in_file.close()
out_file.close()

