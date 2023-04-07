import pandas as pd

raw_data_path = 'data_preprocessing/data_raw/'

def read_data(file: str):
    df = pd.read_csv(raw_data_path + file)
    return df

def process_data(codeforces_data: pd.DataFrame):
    # needed columns: ['problem_statement', 'problem_tags']
    # rename columns as: ['description', 'related_topics']
    codeforces_data = codeforces_data.rename(columns={'problem_statement': 'description', 'problem_tags': 'related_topics'})
    # drop unnecessary columns
    codeforces_data = codeforces_data[['description', 'related_topics']]
    
    all_topics = {}
    for index, row in codeforces_data.iterrows():
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
        codeforces_data[topic] = 0
    for index, row in codeforces_data.iterrows():
        topics = str(row['related_topics']).split(',')
        for topic in topics:
            codeforces_data.at[index, topic] = 1
    # drop related_topics column
    codeforces_data = codeforces_data.drop(columns=['related_topics'])
    print(codeforces_data.head())
    return codeforces_data

if __name__ == '__main__':
    codeforces_data = read_data('codeforces_questions.csv')
    codeforces_data = process_data(codeforces_data)
    # save to csv
    codeforces_data.to_csv('data/codeforces.csv', index=False)