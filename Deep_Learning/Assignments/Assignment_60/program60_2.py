import math
import sys

import numpy as np

import matplotlib.pyplot as plt

x1 = int(input("Enter input : "))

if x1 < -10 or x1 > 10:
    print("Enter input in range between -10 and 10")
    sys.exit()

w1 = 0.4
bias = 0.5

def Sigmoid(z):
    return 1 / (1 + math.exp(-z))

def Relu(z):
    return max(0,z)

def Tanh(z):
    return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))

# calcualte weighted sum
weighted_sum = (x1*w1) + bias
print("Weighted sum of one single neuron :",weighted_sum)

output = Sigmoid(weighted_sum)
print("Output after Sigmoid Activation :",output)

output = Relu(weighted_sum)
print("Output after applying ReLU Activation :",output)

output = Tanh(weighted_sum)
print("Output after applying Tanh Activation :",output)

# generate value for graphs 
x = np.linspace(-10,10,200)

# apply activation functions
sigmoid_y = [Sigmoid(i) for i in x]
relu_y = [Relu(i) for i in x]
tanh_y = [Tanh(i) for i in x]

#-------------------------------------
# Sigmoid Graph
#-------------------------------------
plt.figure(figsize=(6,4))
plt.plot(x, sigmoid_y, label="Sigmoid")
plt.scatter(weighted_sum, Sigmoid(weighted_sum),label="Output point")
plt.title("Sigmoid ACtivation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.show()

#-------------------------------------
# Relu Graph
#-------------------------------------
plt.figure(figsize=(6,4))
plt.plot(x, relu_y, label="ReLU Curve")
plt.scatter(weighted_sum , Relu(weighted_sum) , label="Output Point")
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.legend()
plt.show()

#-------------------------------------
# Tanh Graph
#-------------------------------------
plt.figure(figsize=(6,4))
plt.plot(x , tanh_y , color='purple' ,label='Tanh Curve')
plt.scatter(weighted_sum , Tanh(weighted_sum), label='Output Point')
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.show()