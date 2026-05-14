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

def Pooling(data):

    rows, cols = data.shape

    output_rows = rows // 2
    output_cols = cols // 2

    output = np.zeros((output_rows, output_cols))

    print("\n==============================")
    print("MAX POOLING")
    print("==============================")

    r = 0

    for i in range(0, rows, 2):

        c = 0

        for j in range(0, cols, 2):

            block = data[i:i+2, j:j+2]

            if block.shape != (2, 2):
                continue

            max_value = np.max(block)
            output[r][c] = max_value

            print(f"\nPooling Block -> Output[{r}][{c}]")
            print(block)
            print("Max =", max_value)

            c += 1

        r += 1

    print("\nFinal Pooling Output:")
    print(output)

    return output

pooling_out = Pooling(feature_map)
print(pooling_out)

def Flatten(data):
    print("\n==============================")
    print("FLATTEN LAYER")
    print("==============================")

    print("\nInput:")
    print(data)

    flat = data.flatten()

    print("\nFlattened Output:")
    print(flat)

    return flat

flatten_out = Flatten(pooling_out)
