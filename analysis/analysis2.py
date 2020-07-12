import ibm_boto3
from botocore.client import Config
import pandas as pd


fp = get_file('NRC-Emotion-Intensity-Lexicon-v1.txt')
emolex_df = pd.read_csv(fp,names=["word", "emotion", "association"],sep='\t')
emolex_df = emolex_df[1:]

emolex_words = emolex_df.pivot(index='word',
                                   columns='emotion',
                                   values='association').reset_index()
emotions = emolex_words.columns.drop('word')

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.tag import pos_tag
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import re, string
lemmatizer = WordNetLemmatizer()

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        #token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
        #               '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        #token = re.sub('(@[A-Za-z0-9_]+)','', token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stopwords.words():
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

import types
import pandas as pd
from botocore.client import Config
import ibm_boto3
#Dataframe jdf
jdf = pd.read_csv(body) 

!pip install tweet-preprocessor
import preprocessor as p
import numpy as np
#nltk.download('stopwords')
stop_words = stopwords.words('english')

#p.set_options(p.OPT.URL,p.OPT.MENTION)
p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.NUMBER,p.OPT.HASHTAG, p.OPT.EMOJI)
emo_df = pd.DataFrame(0, index=jdf.index, columns=emotions)
new_jdf = pd.DataFrame()
new_jdf['Sno'] = jdf['Unnamed: 0']
new_jdf['Tweet'] = jdf['Tweet Content']
for emotion in emotions:
    new_jdf[emotion] = 0.0

new_jdf = new_jdf[:100000]
new_jdf = new_jdf.sample(frac=0.1)
#print(new_jdf.head())

def sentiment_score(row):
    tweet = row['Tweet']
    tweet = p.clean(tweet)
    tokens = remove_noise(set(word_tokenize(tweet)),stop_words)
    
    for token in tokens:
        #print(token)
        emo_score = emolex_words[emolex_words.word == token]
        if not emo_score.empty:
            for emotion in list(emotions):
                if not emo_score[emotion].isna().bool():
                    row[emotion] = float(row[emotion]) + float(emo_score[emotion].iloc[0])
    return row

l = []
#print(sentiment_score(new_jdf.iloc[27]))


for i in range(0,len(new_jdf)):
    l.append(sentiment_score(new_jdf.iloc[i]))

    
import csv
csvfile = open('new.csv', 'w')
csvwriter = csv.writer(csvfile)
for item in l:
    csvwriter.writerow(item)
csvfile.close()

#results are stored into a csv file
