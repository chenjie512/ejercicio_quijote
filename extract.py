from random import random
import sys

def main(filename, outputname, ratio):
    file = open(filename)
    output = open(outputname, 'w')
    for line in file:
        if random() <= ratio:
            output.write(line)
    file.close()
    output.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <filename> <output> <ratio>")
        exit(1)
    filename = sys.argv[1]
    output = sys.argv[2]
    ratio = float(sys.argv[3])
    main(filename, output, ratio)
