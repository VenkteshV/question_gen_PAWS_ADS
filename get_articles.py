import wikipedia
import pandas as pd 

final_data = {'topic':[],'summary':[]}
data = pd.read_csv("iir-ground-truth_filtered.tsv",sep="\t")
for index,row in data.iterrows():
    topics = row[1].split(",")
    for topic in topics:
            try:
                related_topics = wikipedia.search(topic)
                summary = wikipedia.summary(topic)
                final_data['topic'].append(topic)
                final_data['summary'].append(summary)
                for rel_topic in related_topics:
                    try:
                        summary = wikipedia.summary(rel_topic)
                        final_data['topic'].append(rel_topic)
                        final_data['summary'].append(summary)
                        final_data1 = pd.DataFrame(final_data)
                        print(final_data1)
                        final_data1.to_csv("article_data.csv",index=False)
                    except:
                        print("here")
                        continue
            except:
                print("here")
                continue
            