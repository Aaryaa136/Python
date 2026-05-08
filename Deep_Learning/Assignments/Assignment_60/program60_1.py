#-----------------------------------------
# Program : Manual calculation of weighted sum
#           and applying Sigmoid activation function
# Input : Nth
# Output : Weighted sum , Sigmoid activation fun output
#-----------------------------------------

import math

x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

# calcualte weighted sum
weighted_sum = (x1*w1 + x2*w2) + bias
print("Weighted sum of one single neuron :",weighted_sum)

# apply sigmoid activation
z = weighted_sum

output = 1 / (1 + math.exp(-z))
print("Output after applying Sigmoid activation function :",output)

if output > 0.5:
    print("Positive class")
else:
    print("Negative class")