import numpy as np

def Flatten(data):
    print("\n==============================")
    print("FLATTEN LAYER")
    print("==============================")

    data = np.array(data)   # convert list → numpy array

    print("\nInput:")
    print(data)

    flat = data.flatten()

    print("\nFlattened Output:")
    print(flat)

    return flat


matrix = [
    [6, 4],
    [8, 6]
]

flatten_output = Flatten(matrix)
