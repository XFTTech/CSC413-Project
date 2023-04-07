# read csv data
import pandas as pd

raw_data_path = 'data_preprocessing/data_raw/'

def read_data(file: str):
    df = pd.read_csv(raw_data_path + file)
    return df

if __name__ == '__main__':
    leetcode_data = read_data('leetcode_questions.csv')
    columns = leetcode_data.columns
    # needed columns: ['Question ID', 'Question Title', 'Question Slug', 'Topic Tagged text', 'Question Text', 'Similar Questions ID']
    # drop unnecessary columns
    leetcode_data = leetcode_data[['Question Title', 'Question Slug', 'Topic Tagged text', 'Question Text']]
    # first drop rows with no Question Text or Topic Tagged text
    for index, row in leetcode_data.iterrows():
        if pd.isnull(row['Question Text']) or pd.isnull(row['Topic Tagged text']):
            leetcode_data = leetcode_data.drop(index)
    
    all_topics = set()
    for index, row in leetcode_data.iterrows():
        topics = str(row['Topic Tagged text']).split(',')
        for topic in topics:
            all_topics.add(topic)
    # represent topics using 1 and 0 using each topic as a column
    for topic in all_topics:
        leetcode_data[topic] = 0
    for index, row in leetcode_data.iterrows():
        topics = str(row['Topic Tagged text']).split(',')
        for topic in topics:
            leetcode_data.at[index, topic] = 1
    # drop Topic Tagged text column
    leetcode_data = leetcode_data.drop(columns=['Topic Tagged text'])
    print(leetcode_data.head())
    # save to csv
    leetcode_data.to_csv('data/leetcode.csv', index=False)