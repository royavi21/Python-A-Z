import numpy as np

prices = np.array([100, 200, 300])
discount = 10 # discount percentage

final_prices = prices - (prices * discount / 100)
print(final_prices)

# array operations are generally faster and use less memory compared to for loops
# convert array using numpy for efficient computation