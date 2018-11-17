from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import csv

#initialize array of comments and upvotes.
comments = {}
upvotes = {}
commentID = {}
filtered_comment = []

#set stopwords
stop_words = set(stopwords.words("english"))

#Open up the csv file and extract the comments and # of upvotes.
with open('lifestyle_drunk.csv') as csv_file:
	csv_reader = csv.reader(csv_file)

	i=0

	for line in csv_reader:
		comments[i] = line[0]
		upvotes[i] = line[6]
		commentID[i] = line[4]

		words = word_tokenize(comments[i])

		#stopwords filter
		for w in words:
			if w not in stop_words:
					filtered_comment.append(w)

		#generate the word frequency distribution for each comment
		#fdist = FreqDist(filtered_comment)

		#with open('test.csv', 'w', newline='') as f:
			#thewriter = csv.writer(f)
			#thewriter.writerow(fdist)

		

		i=i+1

		#filtered_comment = []
#print(filtered_comment)
fdist = FreqDist(filtered_comment)
print(fdist.most_common(len(fdist)))
print(len(fdist))
