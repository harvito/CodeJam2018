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
with open('circlejerk.csv') as csv_file:
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

i=0
j=0
counter=0

commentFreq = []

with open('test.csv', 'w+', newline='') as f:
	thewriter = csv.writer(f)
	for g in fdist:
		thewriter.writerow(fdist)
		break

	with open('circlejerk.csv') as csv_file:
		csv_reader = csv.reader(csv_file)

		for line in csv_reader:

			comments[i] = line[0]
			upvotes[i] = line[6]
			commentID[i] = line[4]

			words = word_tokenize(comments[i])

			print(words)
			for f in fdist:
				for w in words:
					#print(w + " " +f)
					if(w==f):
						counter=counter+1
						#print(counter)

				commentFreq.append(counter)
				counter=0

			commentFreq.append(upvotes[i])
			commentFreq.append(commentID[i])
			print(commentFreq)
			thewriter.writerow(commentFreq)
			commentFreq=[]
