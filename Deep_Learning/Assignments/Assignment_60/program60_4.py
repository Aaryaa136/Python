import math

x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

learning_rate = 0.001

target = 2.1    

for epoch in range(5):
    # calcualte weighted sum
    weighted_sum = (x1*w1 + x2*w2) + bias
    prediction = weighted_sum

    # error
    error = prediction - target
    loss = error ** 2

    # garidents 
    dw1 = 2 * error * x1
    dw2 = 2 * error * x2
    db = 2 * error

    # update weights
    w1  = w1 - learning_rate * dw1
    w2 = w2 - learning_rate * dw2
    bias = bias - learning_rate * db

    print(f"Epoch {epoch + 1}")
    print("Prediction :",prediction)
    print("Loss :",loss)
    print("Updated weights :",w1,w2,bias)
    print("-"*60)