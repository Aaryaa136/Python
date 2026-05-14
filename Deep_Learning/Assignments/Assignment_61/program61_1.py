import numpy as np

from sklearn.preprocessing import StandardScaler

#    age, montly charge, tensure, no of complaints, support calls

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# 0 = customer will stay    1 = customer will leave
y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])