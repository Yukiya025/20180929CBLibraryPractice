"""
1. Open 26and1_600JP.txt OK
2. Split the contents by line break OK
3. Add split contents to 26and1_600.csv OK
"""
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

jp = open('26and1_600JP.txt', 'r')
jp_w = jp.read()
jp_w = jp_w.split()

csv_input = pd.read_csv('26and1.csv', sep=",")
csv_input['Яп'] = ''

for index, row in csv_input.iterrows():
    csv_input['Яп'][index] = jp_w[index]

csv_input.to_csv('26and1.csv', index=False)