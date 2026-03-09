import numpy as np

X = np.array([1,2,3,4,5])
Y = np.array([3,4,2,4,5])

X_mean = np.mean(X)
Y_mean = np.mean(Y)

# Slope
m  = np.sum((X - X_mean) * (Y - Y_mean)) / np.sum((X - X_mean) ** 2)

# Intercept 
C = Y_mean - m * X_mean

# Regression equation
X_new = 6
Y_pred = m * X_new + C

print("Mean of X : ",X_mean)
print("Mean of Y : ",Y_mean)

print("Slope (m) : ",m)
print("Intercept (c) : ",C)

print("Predicted Y for X = 6 ",Y_pred)