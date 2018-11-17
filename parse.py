from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from nltk.probability import FreqDist
import csv

#initialize array of comments and upvotes.
comments = {}
upvotes = {}
commentID = {}

#Open up the csv file and extract the comments and # of upvotes.
with open('entertainment_movies.csv') as csv_file:
	csv_reader = csv.reader(csv_file)

	i=0

	for line in csv_reader:
		comments[i] = line[2]
		upvotes[i] = line[8]
		commentID[i] = line[6]
		print("comment: " + comments[i] + "rating: " + upvotes[i] + " comment id:" + commentID[i])
		i=i+1

#get the frequency distribution of words for each comment.
