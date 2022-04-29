from pyspark import SparkContext
import sys

def main(filename, outputname):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        output = open(outputname, 'w')
        data = sc.textFile(filename)
        words_rdd = data.flatMap(lambda x: x.split())
        output.write(f"Words count of {filename}: ")
        output.write(str(words_rdd.count()))
        output.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <filename> <outputname>")
        exit(1)
    filename = sys.argv[1]
    outputname = sys.argv[2]
    main(filename, outputname)
