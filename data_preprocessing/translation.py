#! pip install googletrans==3.1.0a0

from googletrans import Translator
import pandas as pd

def perform_data_augmentation(df):
    translator = Translator()
    # add new rows by translating from english to chinese then chinese to english
    # first create a copy of the dataframe
    df_cp = df.copy()
    for index, row in df_cp.iterrows():
        # translate from english to chinese
        translated = translator.translate(row['description'], dest='fr')
        # translated = translator.translate(row['description'], dest='zh-cn')
        # translate from chinese to english
        translated = translator.translate(translated.text, dest='en')
        # only change first column (description) while keeping the rest the same
        new_row = row.copy()
        new_row['description'] = translated.text
        # append new row to dataframe
        # df = df.append(new_row, ignore_index=True)
        df = df._append(new_row, ignore_index=True)
        print(index)
    print(df.shape)
    return df

if __name__ == '__main__':
    df = pd.read_csv('data/leetcode.csv')
    # test_row = df.iloc[0]
    # t = Translator()
    # print(df.shape)
    # res = t.translate(test_row['description'], dest='zh-cn')
    # print(res.text)
    # res = t.translate(res.text, dest='en')
    # print(res.text)
    # # append new row to dataframe
    # test_row['description'] = res.text
    # df = df.append(test_row, ignore_index=True)
    # # print last row
    # print(df.iloc[-1])
    df = perform_data_augmentation(df)
    df2 = pd.read_csv('data/leetcode_augmented.csv')
    df2 = df2._append(df, ignore_index=True)
    df2.to_csv('data/leetcode_augmented-2.csv', index=False)
    # save to new csv file