
import matplotlib.pyplot as plt
import numpy as np


def plot_univariate(df, cols):

    fig, axes = plt.subplots(len(cols) // 2, 2, figsize=(12, 4))

    for i, c in enumerate(cols):

        N = df[c].nunique()
        if (N > 10):
            df[c].plot(kind='hist', ax=axes[i // 2, i % 2], title=c)

        elif N <= 10:
            df[c].value_counts().plot(kind='bar', ax=axes[i // 2, i % 2], title=c)

        else:
            pass

    plt.tight_layout()
    plt.suptitle('Univariate Statistics')

    return axes
