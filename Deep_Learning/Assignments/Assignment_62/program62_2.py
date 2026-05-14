import numpy as np

image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

feature_map = np.zeros((3, 3), dtype=int)

for i in range(3):
    for j in range(3):

        region = image[i:i+3, j:j+3]

        multiplied = region * kernel

        result = np.sum(multiplied)

        feature_map[i][j] = result

print(feature_map)


def ReLU(data):
    print("\n==============================")
    print("ReLU ACTIVATION")
    print("==============================")

    output = np.maximum(0, data)

    print("\nInput:")
    print(data)

    print("\nRule: ReLU(x) = max(0, x)")

    print("\nOutput:")
    print(output)

    return output

feature_map = ReLU(feature_map)