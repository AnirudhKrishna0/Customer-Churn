import pandas as pd

data=pd.read_csv("customer_churn_dataset.csv")

#total customers churned or not
#print(data["Churn"].value_counts(normalize=True)*100)

print(data["Churn"].groupby(data["Gender"]).value_counts(normalize=True)*100)

