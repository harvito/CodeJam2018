from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from nltk.probability import FreqDist
import csv

#initialize array of comments and upvotes.
comments = {}
upvotes = {}

#Open up the csv file and extract the comments and # of upvotes.
with open('entertainment_movies.csv') as csv_file:
	csv_reader = csv.reader(csv_file)

	i=0

	for line in csv_reader:
		comments[i] = line[2]
		upvotes[i] = line[8]
		print(comments[i] + upvotes[i])
		i=i+1

#get the frequency distribution of words for each comment.
c = comments[8]

print(c)

c = word_tokenize(c)

print(c)

fdist = FreqDist(c)

fdist.most_common(4)