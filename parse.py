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

		i=i+1


fdist = FreqDist(filtered_comment)
print(fdist.most_common(len(fdist)))
print(len(fdist))

cdist = fdist.most_common(len(fdist))

for f in fdist:
	print(f)


with open('test.csv', 'w+', newline='') as f:
			thewriter = csv.writer(f)
			for g in fdist:
				thewriter.writerow(cdist)
				break
