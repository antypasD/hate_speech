import datasets 
import pandas as pd

# TODO standarize mentions through all datasets
# Measuring Hate Speech 
#hate_speech_score - continuous hate speech measure, where higher = more hateful and lower = less hateful.
#  > 0.5 is approximately hate speech,
#  < -1 is counter or supportive speech,
#  and -1 to +0.5 is neutral or ambiguous.
# TODO check hatespeech column - remove reddit
dataset = datasets.load_dataset('ucberkeley-dlab/measuring-hate-speech', 'binary')   
df = dataset['train'].to_pandas()

# original
df.to_csv('./datasets/measuring_hate_speech.csv', index=False)

# clean
df = df.groupby('comment_id').nth(0)

def map_label(x):
    if x >= -1 and x <= 0.5:
        label = 0 # neutral/ambiguous
    elif x > 0.5:
        label = 1 # hate
    elif x < -1:
        label = -1 # not hate

df['label'] = df['hate_speech_score'].apply(map_label)

df = df.reset_index()
df[['comment_id', 'annotator_id', 'text', 'label']].to_csv('./datasets/measuring_hate_speech_clean.csv', index=False)



# ‘Call me sexist, but’ 
# TODO remove adversarial examples
df = pd.read_csv('./datasets/call_me_sexist_but_data.csv')
df['label'] = df['sexist']
df['label'] = df['label'].map({True:1, False:-1}) # 1 -> sexist, 0 -> not sexist
df[['id', 'text', 'label']].to_csv('./datasets/call_me_sexist_but_data_clean.csv', index=False)
