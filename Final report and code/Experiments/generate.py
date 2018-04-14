import subprocess
import sys, os
import numpy as np

root = "/N/dc2/scratch/lyulianu/caffe/FR-caffe/datasets_new_transformed/train/"

for r, d, f in os.walk(root):
    for fname in f:
        os.chdir(str(r))

        # Random -10 to 10
        deltas = np.random.randint(low=-5, high=6, size=(4, 2, 2))

        for i, delta in enumerate(deltas):
            corners = [(0, 0), (0, 99), (99, 99), (99, 0)]

            # First point
            command = ["convert", fname, "-matte", "-virtual-pixel", "Mirror", "-distort", "Perspective", \
                       str(corners[0][0]) + "," + str(corners[0][1]) + ","+ str(corners[0][0]+delta[0][0]) + "," + str(corners[0][1]+delta[0][1]) + " " + \
                       str(corners[1][0]) + "," + str(corners[1][1]) + ","+ str(corners[1][0]+delta[1][0]) + "," + str(corners[1][1]+delta[1][1]) + " " + \
                       str(corners[2][0]) + "," + str(corners[2][1]) + ","+ str(corners[2][0]-delta[0][0]) + "," + str(corners[2][1]-delta[0][1]) + " " + \
                       str(corners[3][0]) + "," + str(corners[3][1]) + ","+ str(corners[3][0]-delta[1][0]) + "," + str(corners[3][1]-delta[1][1]), str(i)+"_"+fname]
            print(command)
            subprocess.call(command)
