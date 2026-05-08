import math

# actual values
actual_val = [0 , 1, 1]
predicted_value = [0.9 , 0.2 , 0.8]

def MSE(Y , y_p):
    n = len(Y)

    if len(Y) != len(y_p):
        return
    
    loss = 0
    
    for i, j in zip(Y, y_p):
        loss = loss + (i - j) ** 2

    return loss / n

def Binary_Cross(Y , y_p):
    n = len(Y)

    if len(Y) != len(y_p):
        return
    
    bce = 0
    for i , j in zip(Y, y_p):
        bce = bce + -(i * math.log(j) + (1 - i) * math.log(1 - j))

    return bce / n 
    

loss = MSE(actual_val , predicted_value)
print("Mean Square Error :",loss)

bce = Binary_Cross(actual_val , predicted_value)
print("Binary Cross Entropy :",bce)

print("MSE is used for regression problems where outputs are continuous values")
print("Binary Cross Entropy is used for classification problems where outputs are probabilities (0 or 1)")