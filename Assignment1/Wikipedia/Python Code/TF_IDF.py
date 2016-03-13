from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.feature import HashingTF, IDF

sc = SparkContext()

rdd = sc.wholeTextFiles("/usr/local/Cellar/BigDataAdvanced/Assignment1/TwitterStuff/TweetData").map(lambda (name,text):text.split())
tf = HashingTF()
tfVectors = tf.transform(rdd).cache()
a = tfVectors.collect()
count = 0 
for vec in a:
        print vec
        count = count + 1
        with open("TF_Tweet"+str(count)+".txt","w") as f:
                f.write(str(vec))
        f.close()

idf = IDF()
idfModel = idf.fit(tfVectors)
tfIdfVectors = idfModel.transform(tfVectors)
file = open("TF-IDF_tweet.txt", 'w')
file.write(str(tfIdfVectors.collect()))

#count = 0
#output=tfIdfVectors.collect()
#for vec in output:
#	print vec
#	count = count + 1
#	with open("TF_Wiki"+str(count)+".txt","w") as f:
#		f.write(str(vec))
#	f.close()
	
	
