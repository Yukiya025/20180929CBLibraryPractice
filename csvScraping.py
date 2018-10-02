import pandas as pd

def show_word():
    csv_input = pd.read_csv(filepath_or_buffer= r'26and1.csv', sep=",")
    print("=" * 20)

    for i in range(9):
        print(csv_input.iloc[i, 0])
