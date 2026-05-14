import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

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

print("Shape of dataset :")
print(X.shape)

scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

print("\nScaled Data :")
print(X_Scaled)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='adam',
    max_iter=100,
    random_state=42
)

model.fit(X_Scaled, y)

Y_pred = model.predict(X_Scaled)
print(Y_pred)

accuracy = accuracy_score(y , Y_pred)
print("Acurracy score :",accuracy*100)