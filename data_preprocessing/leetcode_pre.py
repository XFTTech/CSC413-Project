import pandas as pd

raw_data_path = 'data_preprocessing/data_raw/'

def read_data(file: str):
    df = pd.read_csv(raw_data_path + file)
    return df

def process_data(leetcode_data: pd.DataFrame):
    print(leetcode_data.columns)
    # needed columns: ['id', 'title', 'description', 'related_topics']
    # drop unnecessary columns
    leetcode_data = leetcode_data[['id', 'title', 'description', 'related_topics']]
    # first drop rows with no description or related topics
    for index, row in leetcode_data.iterrows():
        if pd.isnull(row['description']) or pd.isnull(row['related_topics']):
            leetcode_data = leetcode_data.drop(index)
    
    all_topics = {}
    for index, row in leetcode_data.iterrows():
        topics = str(row['related_topics']).split(',')
        for topic in topics:
            if topic not in all_topics:
                all_topics[topic] = 1
            else:
                all_topics[topic] += 1
    # sort topics by frequency
    all_topics = sorted(all_topics.items(), key=lambda x: x[1], reverse=True)
    all_topics_keys = [topic[0] for topic in all_topics]
    # represent topics using 1 and 0 using each topic as a column
    for topic in all_topics_keys:
        leetcode_data[topic] = 0
    for index, row in leetcode_data.iterrows():
        topics = str(row['related_topics']).split(',')
        for topic in topics:
            leetcode_data.at[index, topic] = 1
    # drop related_topics column
    leetcode_data = leetcode_data.drop(columns=['related_topics'])
    print(leetcode_data.head())
    return leetcode_data

if __name__ == '__main__':
    leetcode_data = read_data('leetcode_dataset - lc.csv')
    leetcode_data = process_data(leetcode_data)
    # save to csv
    leetcode_data.to_csv('data/leetcode.csv', index=False)