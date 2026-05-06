import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

df = pd.DataFrame(data.data , columns=data.feature_names)
df["target"] = data.target

# to write data in csv
df.to_csv("breast_cancer.csv" , index = False)

print("breast_cancer.csv file gets created successfully")