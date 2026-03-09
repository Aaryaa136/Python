import numpy as np
import matplotlib.pyplot as plt

# X : Experience     y : Salary
X = np.array([1,2,3,4,5])
Y = np.array([20000,25000,30000,35000,40000])

Data = [[X],[Y]]

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

print("Predicted Salary for 6 Years of Experience ",Y_pred)

Y_line = m * X + C

plt.scatter(X , Y , color = "blue" , label = "Data points")

plt.plot(X , Y_line , color = "red" , label = "Regression Line")

plt.xlabel("X : Experience(Years)")
plt.ylabel("Y : Salary")

plt.legend()
plt.show()