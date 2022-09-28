def plot():
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        import seaborn as sns
    except ModuleNotFoundError:
        return

    s = pd.Series([1, 2, 2.5, 3, 3.5, 4, 5])
    ax = s.plot.kde()
    plt.show()


plot()
