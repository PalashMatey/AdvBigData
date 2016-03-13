
from pyspark import SparkContext
import math

def main():
    sc = SparkContext()
    companies = ["apple","facebook","google","ibm","walmart"]
    for comp in companies:
        textfile = comp+"_quotes.txt"
        rdd = sc.textFile(textfile)
        rdd = rdd.map(lambda string: float(string))
        stats = rdd.stats()
        stddev = stats.stdev()
        outliers = rdd.filter(lambda x: math.fabs(x - stats.mean()) > 2 * stddev)
        print "For company :",comp
        print "Outliers are :"
        print outliers.collect()


if __name__=='__main__':
    main()
