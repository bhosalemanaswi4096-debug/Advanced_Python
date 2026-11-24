
import pandas as pd
import numpy as np

numbers = np.random.randint(1, 101, 10)

series = pd.Series(numbers)

print("Pandas Series:")
print(series)
