from nltk.tokenize import word_tokenize
# from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import csv
import os

spath = r"/Users/daesun/Documents/GitHub/CodeJam2018/NoBlanksNoRepeats"

filenames = os.listdir("./NoBlanksNoRepeats/NoBlanksNoRepeats")
# print "filenames: ", filenames

# os.chdir("/Users/daesun/Documents/GitHub/CodeJam2018/NoBlanksNoRepeats")


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
	# print(current_file)
	comments = {}
	upvotes = {}
	commentID = {}
	filtered_comment = []

	#set stopwords
	stop_words = set(stopwords.words("english"))

	print "z"
	#Open up the csv file and extract the comments and # of upvotes.
	try:
		csv_file = open("./NoBlanksNoRepeats/NoBlanksNoRepeats/"+current_file)
	except:
		print current_file
		continue

	csv_reader = csv.reader(csv_file)

	i=0
	print "a"
    # extract unique words in file
	for line in csv_reader:
		# print(i+1)
		comments[i] = line[0]
		upvotes[i] = line[6]
		commentID[i] = line[4]

		words = comments[i].split()
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
	print "marker"

	commentFreq = []
    # extract info and write
	with open("newfile.csv", 'w+') as file:
		print("opened", file)
		thewriter = csv.writer(file)
		#for g in fdist:
		#	print "<", g, ">"
		thewriter.writerow(fdist.items())
		#	break

		with open("./NoBlanksNoRepeats/NoBlanksNoRepeats/"+current_file) as csv_file:
			csv_reader = csv.reader(csv_file)

			for line in csv_reader:

				comments[i] = line[0]
				upvotes[i] = line[6]
				commentID[i] = line[4]

				words = comments[i].split()

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