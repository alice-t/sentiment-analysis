import re
import json
import sys
import preprocessor.api as p
from preprocessor.api import clean, tokenize, parse, clean_file
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#If writing in Jupyter Notebooks, use this format to install packages using pip directly
#!{sys.executable} -m pip install vaderSentiment


#clean file using preprocessor package
input_file_name = "pawboamazon.txt"
p.clean_file(input_file_name)


#remove duplicate lines
#fyi this is needed as the preprocessor cleaning above removes URLs, hashtags, emojis etc., but not duplicate lines.
lines_seen = set() # holds lines already seen
with open("pawboamazon_clean_final.txt", "w") as output_file:
    for each_line in open("clean_pawboamazon.txt", "r"):
        if each_line not in lines_seen: # check if line is not duplicate
            output_file.write(each_line)
            lines_seen.add(each_line)

            
#count lines in original file
orig_count = 0
clean_count = 0
for each_line in open("clean_pawboamazon.txt", "r"):
    orig_count+=1
print(orig_count)


#count lines in final cleaned file
for each_line in open("pawboamazon_clean_final.txt", "r"):
    clean_count+=1
print(clean_count)


#sentiment analysis using VADER package
analyser = SentimentIntensityAnalyzer()


#counter for number of positive/neutral/negative statements
pos_count = 0
neu_count = 0
neg_count = 0

def sentiment_analyzer_scores(sentence):
    
    global pos_count
    global neu_count
    global neg_count
       
    score = analyser.polarity_scores(sentence)
    print(sentence)
    print('Pos score:', score['pos'])
    print('Neu score:', score['neu'])
    print('Neg score:', score['neg'])
    print('Compound score:', score['compound'])
    if score['compound'] >= 0.05:
        print("Overall = Positive") 
        pos_count+=1
    elif score['compound'] <= -0.05:
        print("Overall = Negative")
        neg_count+=1
    else:
        print("Overall = Neutral")
        neu_count+=1
    print("-------------")
    
with open("pawboamazon_clean_final.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        sentiment_analyzer_scores(line)
        
print("Number of positive statements", pos_count)
print("Number of neutral statements", neu_count)
print("Number of negative statements", neg_count)


# ## The code below is to detect the amount of positive and negative words in the txt file. The corpus of positive and negative words (~6800 words) or 'Opinion Lexicon' can be found here:
# ### https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html?ref=hackernoon.com

"""
# save the positive words into a list called p_list
with open('positive.txt') as f:
    p_txt = f.read()
    p_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', p_txt)
    p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if cool is in the list
    #print 'cool is in the postive list: ', 'cool' in p_list 

# save the negative words into a list called n_list
with open('negative.txt') as f:
    n_txt = f.read()
    n_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', n_txt)
    n_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if abrade is in the list
    #print 'abrade is in the negative list: ', 'abrade' in n_list 
    # test if cool is in the list
    #print 'cool is in the negative list: ', 'cool' in p_list 
    
print(p_txt)
"""


"""
# process the tweets
with open('furbotweets.txt', errors='ignore') as f:

    txt = f.read()
    txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', txt)    
    word_list = txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    
    print(txt)
    
    
    
    # create empty dictionaries
    word_count_dict = {}
    word_count_positive = {}
    word_count_negative= {}
    
    for word in word_list:
        # count all words frequency
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
        # count if it is a positive word
        if word in p_list:
            if word in word_count_positive.keys():
                word_count_positive[word] += 1
            else:
                word_count_positive[word] = 1
        # else see if it is a negative word
        elif word in n_list:
            if word in word_count_negative.keys():
                word_count_negative[word] += 1
            else:
                word_count_negative[word] = 1
        else: # do nothing
            pass

    list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
    list_positive = sorted(word_count_positive.items(), key=lambda x:x[1], reverse=True)
    list_negative = sorted(word_count_negative.items(), key=lambda x:x[1], reverse=True)

    with open('word_count.csv', 'w')as f1:
        for i in list_dict:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_positive.csv', 'w')as f1:
        for i in list_positive:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_negative.csv', 'w')as f1:
        for i in list_negative:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
"""

