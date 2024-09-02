import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(data, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.show()
#function
def plot_scatter(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column])
    plt.title(f'Scatter Plot of {x_column} vs {y_column}')
    plt.show()
