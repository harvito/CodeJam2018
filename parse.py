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
		#
		for w in words:
			if w not in stop_words:
					filtered_comment.append(w)

		fdist = FreqDist(filtered_comment)

		print(filtered_comment)
		print(fdist.most_common(len(fdist)))

		i=i+1

		filtered_comment = []

#get the frequency distribution of words for each comment.
