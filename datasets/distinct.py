import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("symtoms_df.csv")

# Get distinct values from Symptom_1 column
distinct_symptom_1 = df['Symptom_1'].unique()

# Get distinct values from Symptom_2 column
distinct_symptom_2 = df['Symptom_2'].unique()

# Get distinct values from Symptom_3 column
distinct_symptom_3 = df['Symptom_3'].unique()

# Get distinct values from Symptom_4 column
distinct_symptom_4 = df['Symptom_4'].unique()

print("Distinct values in Symptom_1:", distinct_symptom_1)
print("Distinct values in Symptom_2:", distinct_symptom_2)
print("Distinct values in Symptom_3:", distinct_symptom_3)
print("Distinct values in Symptom_4:", distinct_symptom_4)