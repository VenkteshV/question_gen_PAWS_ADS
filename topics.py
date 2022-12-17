import wikipedia
import pandas as pd 

final_data = {'topic':[],'summary':[]}
data = pd.read_csv("iir-ground-truth_filtered.tsv",sep="\t")
count =0
for index,row in data.iterrows():
    topics = row[1].split(",")
    for topic in topics:
        count+=1
        print(count)    