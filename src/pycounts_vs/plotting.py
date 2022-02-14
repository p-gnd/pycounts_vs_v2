import matplotlib.pyplot as plt

def plot_words(word_counts, n=10):
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig

from pycounts_vs.pycounts_vs import count_words
from pycounts_vs.plotting import plot_words
counts = count_words("zen.txt")
fig = plot_words(counts, 10)