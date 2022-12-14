import datasets 
import pandas as pd

# TODO standarize mentions through all datasets
# TODO check hatespeech column - remove reddit

import datasets 
import pandas as pd

# Measuring Hate Speech 
#hate_speech_score - continuous hate speech measure, where higher = more hateful and lower = less hateful.
#  > 0.5 is approximately hate speech,
#  < -1 is counter or supportive speech,
#  and -1 to +0.5 is neutral or ambiguous.


def map_label(x):
    if x >= -1 and x <= 0.5:
        label = 0 # neutral/ambiguous
    elif x > 0.5:
        label = 1 # hate
    elif x < -1:
        label = -1 # not hate

    return label

dataset = datasets.load_dataset('ucberkeley-dlab/measuring-hate-speech', 'binary')   
df = dataset['train'].to_pandas()

# original
df.to_csv('./datasets/measuring_hate_speech.csv', index=False)

# clean
df = df.groupby('comment_id').nth(0)
# get only text from Twitter
df = df[df['platform'] == 2]

df['label'] = df['hate_speech_score'].apply(map_label)

df = df.reset_index()
df[['comment_id', 'annotator_id', 'text', 'label']].to_csv('./datasets/measuring_hate_speech_clean.csv', index=False)



