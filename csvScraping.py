import pandas as pd

def show_word():
    csv_input = pd.read_csv(filepath_or_buffer= r'26and1.csv', sep=",")
    # print(csv_input[["Ру", "Ном"]])
    print("=" * 20)
    print(csv_input.iloc[2, 0])
