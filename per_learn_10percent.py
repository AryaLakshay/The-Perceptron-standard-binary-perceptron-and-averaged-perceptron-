import sys;
import os;
from random import shuffle;
from array import *;


def per_learn():
    # if len(sys.argv)!=2:
    #	print("INVALID Commandline Input");
    #    sys.exit();

    fileDir = sys.argv[1];

    # fileDir = "/Users/lakshayarya/Desktop/CSCI 544 Assingment-1/Assingment-1/Spam or Ham/train";

    HamSpamWeights = {};
    fileData = {}
    fileList = [];

    if not os.path.isdir(fileDir):
        print("INVALID File Directory");
        sys.exit();

    for root, dirs, files in os.walk(fileDir):
        count = len(files);
        count = (count // 10) + 1;
        done = 0;
        for name in files:
            if name.endswith(".txt"):
                done = done + 1;
                if (done > count):
                    break;
                fileList.append(root + "//" + name);

    bias = 0;
    y = 0;
    i = 0;

    while i < 20:

        shuffle(fileList)

        for pathName in fileList:

            if pathName.endswith("ham.txt"):
                y = -1
            else:
                y = 1

            alpha = 0

            if pathName in fileData:
                for word in fileData[pathName].split():
                    if word not in HamSpamWeights:
                        HamSpamWeights[word] = 0
                    else:
                        alpha += HamSpamWeights[word]

                result = alpha + bias;
                result = result * y;

                if result > 0:
                    pass
                else:
                    if y == 1:
                        bias += 1
                        for word in fileData[pathName].split():
                            HamSpamWeights[word] += 1
                    else:
                        bias -= 1
                        for word in fileData[pathName].split():
                            HamSpamWeights[word] -= 1

            else:
                f = open(pathName, "r", encoding="latin1");

                fileString = ""
                for line in f:
                    for word in line.split():
                        fileString += word
                        fileString += " "
                        if word not in HamSpamWeights:
                            HamSpamWeights[word] = 0
                        else:
                            alpha += HamSpamWeights[word]

                result = alpha + bias;
                result = result * y;

                fileData[pathName] = fileString

                f.seek(0);

                if result > 0:
                    pass
                else:
                    if y == 1:
                        bias += 1
                        for lin in f:
                            for word in lin.split():
                                HamSpamWeights[word] += 1
                    else:
                        bias -= 1
                        for lin in f:
                            for word in lin.split():
                                HamSpamWeights[word] -= 1

        i += 1
        print(i);

    outf = open("per_model.txt", "w", encoding="latin1");
    outf.write(str(bias));
    outf.write("\n");
    for key, value in HamSpamWeights.items():
        outf.write(key);
        outf.write(" ");
        outf.write(str(value));
        outf.write("\n");

    outf.close();


per_learn();