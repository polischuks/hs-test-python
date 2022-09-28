def plot():
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
    except ModuleNotFoundError:
        return

    fig, ax = plt.subplots(figsize=(1, 2))

    ax.boxplot([1, 2, 3, 4])
    plt.boxplot([1, 2, 3, 4])

    plt.show()


plot()
