import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    """Load CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def show_basic_statistics(df):
    """Display basic statistics of the dataset."""
    print("\nBasic Statistics:")
    print(df.describe())

def plot_data(df, column):
    """Plot histogram of a given column."""
    if column in df.columns:
        plt.hist(df[column], bins=20, edgecolor='black')
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {column}")
        plt.show()
    else:
        print(f"Column '{column}' not found in the dataset.")

def main():
    filename = "data.csv"  # Change this to your dataset filename
    df = load_data(filename)
    
    if df is not None:
        show_basic_statistics(df)
        column_to_plot = input("Enter column name to plot: ")
        plot_data(df, column_to_plot)

if __name__ == "__main__":
    main()