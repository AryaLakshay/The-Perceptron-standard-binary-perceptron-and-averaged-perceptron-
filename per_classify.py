import sys;
import os;
from math import log

def per_classify():

    f = open("per_model.txt", "r", encoding="latin1");

    HamSpamWeights = {}
    bias=0
    count=0

    for line in f:
        count += 1
        if count == 1:
            bias = int(line)
        else:
            splitted = line.split()
            HamSpamWeights[splitted[0]] = int(splitted[1])


    filedir="/Users/lakshayarya/Desktop/CSCI 544 Assingment-1/Assingment-1/Spam or Ham/dev"
    #filedir = sys.argv[1];
    if not os.path.isdir(filedir):
        print("Invalid Directory");
        sys.exit();

    outf = open("per_output.txt", "w", encoding="latin1");
    for root, dirs, files in os.walk(filedir):
        for name in files:
            if name.endswith(".txt"):
                f = open(root + "//" + name, "r", encoding="latin1");

                alpha = 0;
                for line in f:
                    for word in line.split():
                        if word in HamSpamWeights:
                             alpha +=HamSpamWeights[word]

                alpha +=bias

                if alpha>0:
                    outf.write("spam " + root + "/" + name + "\n");
                else:
                    outf.write("ham " + root + "/" + name + "\n");


per_classify()
