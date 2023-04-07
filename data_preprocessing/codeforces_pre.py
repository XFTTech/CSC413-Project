import pandas as pd

raw_data_path = 'data_preprocessing/data_raw/'

def read_data(file: str):
    df = pd.read_csv(raw_data_path + file)
    return df

def process_data(codeforces_data: pd.DataFrame):
    print(codeforces_data.columns)
    return codeforces_data

if __name__ == '__main__':
    codeforces_data = read_data('codeforces_questions.csv')
    codeforces_data = process_data(codeforces_data)
    # save to csv
    # codeforces_data.to_csv('data/codeforces.csv', index=False)