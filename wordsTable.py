from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import csv
import sys
import os

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# set stopwords
stop_words = set(stopwords.words("english"))
stop_words.add("nt") # redditers do'nt know how to spell or are linking nt.reddit...

files = os.listdir("./NoBlanksNoRepeats/NoBlanksNoRepeats")
outf = open('words.csv', 'w')
outf.write("w, sr, f, cf, cs\n")

for file in files:
    csv_file = open("./NoBlanksNoRepeats/NoBlanksNoRepeats/" + file)
    flen = file_len("./NoBlanksNoRepeats/NoBlanksNoRepeats/" + file)
    csv_reader = csv.reader(csv_file)
    
    # empty dictionaries
    wordsd = { }
    cmntcnt = { }
    cmntscr = { }
    
    i = 1
    for line in csv_reader:
        # print progress
        print "\rFile", file, "line", i, "/", flen,
        sys.stdout.flush()
        
        # reset checked words
        checkedWordsThisComment = [ ]
        
        cmnt = line[0]
        subreddit = line[2]
        try:
            rate = int(float(line[6]))
        except:
            print "blank rating in file", file, "on line", i, "\b, skipping"
            continue
        
        
        
        words = cmnt.split()
        
        for word in words:
            # update occurrence dictionary
            if word in wordsd:
                wordsd[word] += 1
            else:
                wordsd[word] = 1
            
            # update cmntcnt and cmntscr
            if word not in checkedWordsThisComment:
                checkedWordsThisComment.append(word)
                if word in cmntcnt:
                    cmntcnt[word] += 1
                else:
                    cmntcnt[word] = 1
                
                if word in cmntscr:
                    cmntscr[word] += rate
                else:
                    cmntscr[word] = rate
        i += 1
    # end of one subreddit
    csv_file.close()
    
    # write to our output file
    a = len(wordsd)
    i = 1
    for w in wordsd:
        if w in stop_words:
            continue
        print "\rWriting to csv for", file, i, "of", a,
        sys.stdout.flush()
        outf.write(w + ", " + subreddit+ ", " + str(wordsd[w]) + ", " + str(cmntcnt[w]) + ", " + str(cmntscr[w]) + "\n")
        i += 1

outf.close()