import sys
import json




#per_row = []
#for line in a_file:
#    per_row.append(line.split('\t'))

#per_column = zip(*per_row)

#scored_words = per_column[0]

#somedict = dict()

def scores_tweet(tweet_file, scores):
    "Calculate scores for all tweets in tweet_file"
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '') for line in f)
        return [score_tweet(tweet, scores) for tweet in tweets]

def report_scores(sent_file):
    with open(sent_file) as k:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in k}

def score_tweet(tweet, scores):
    "Returns the score for a tweet or 0 if it's not in AFINN-111.txt"
    return sum(scores.get(word, 0) for word in tweet.split())


def make_cols(sent_file):
    
    with open(sent_file) as k:
        per_row = []
        for line in k:
            per_row.append(line.strip().split('\t'))

        per_column = zip(*per_row)
        scored_words = list(per_column[0])
        scored_nums = list(per_column[1])  
        scored_dict = dict(zip(scored_words, scored_nums))
        #print scored_dict


if __name__ == '__main__':
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    with open(sent_file) as k:
        per_row = []
        for line in k:
            per_row.append(line.strip().split('\t'))

        per_column = zip(*per_row)
        scored_words = list(per_column[0])
        scored_nums = list(per_column[1])  
        scored_dict = dict(zip(scored_words, scored_nums))
    #for word in scored_dict:
     #   print int(scored_dict[word]) 

    with open(sent_file) as l:
       linesum = []         
       for line in l:
            for word in line:
                linesum[line] += int(scored_dict[word])

    print linesum














