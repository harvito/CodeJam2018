from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import csv
import os

spath = r"/Users/daesun/Documents/GitHub/CodeJam2018/NoBlanksNoRepeats"

filenames = os.listdir(spath)

os.chdir("/Users/daesun/Documents/GitHub/CodeJam2018/NoBlanksNoRepeats")


newfiles = {}
i=0

for filename in filenames:
	newfiles[i] = "New_"+ str(filename)
	i = i+1

i=0

number_of_files = len(filenames)
loop_counter = 0


#initialize array of comments and upvotes.
for current_file in filenames:
	print(current_file)
	comments = {}
	upvotes = {}
	commentID = {}
	filtered_comment = []

	#set stopwords
	stop_words = set(stopwords.words("english"))

	#Open up the csv file and extract the comments and # of upvotes.
	try:
		csv_file = open(filenames[loop_counter])
	except:
		print(filenames[loop_counter])

	csv_reader = csv.reader(csv_file)

	i=0
	
	for line in csv_reader:
		print(i+1)
		comments[i] = line[0]
		upvotes[i] = line[6]
		commentID[i] = line[4]

		words = word_tokenize(comments[i])

		#stopwords filter
		for w in words:
			if w not in stop_words:
					filtered_comment.append(w)
	
		i=i+1
	csv_file.close()

	fdist = FreqDist(filtered_comment)

	cdist = fdist.most_common(len(fdist))

	i=0
	j=0
	counter=0

	commentFreq = []

	with open(newfiles[loop_counter], 'w+', newline='') as file:
		thewriter = csv.writer(file)
		for g in fdist:
			thewriter.writerow(fdist)
			break

		with open(filenames[loop_counter]) as csv_file:
			csv_reader = csv.reader(csv_file)

			for line in csv_reader:

				comments[i] = line[0]
				upvotes[i] = line[6]
				commentID[i] = line[4]

				words = word_tokenize(comments[i])

				for f in fdist:
					for w in words:
						if(w==f):
							counter=counter+1

					commentFreq.append(counter)
					counter=0

				commentFreq.append(upvotes[i])
				commentFreq.append(commentID[i])
				#print(commentFreq)
				thewriter.writerow(commentFreq)
				commentFreq=[]
		csv_file.close()
	file.close()
	loop_counter = loop_counter+1