
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/raw/telco_churn.csv")

# Preview
print(df.head())
print(df.info())

# Basic stats
print("Total customers:", len(df))
print("Churn rate:", df['Churn'].value_counts(normalize=True)['Yes'] * 100, "%")

# Simple plot - churn distribution
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()

# Churn by Contract Type
plt.figure(figsize=(6,4))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Churn by Contract Type")
plt.ylabel("Number of Customers")
plt.show()

# Churn by Tenure Bucket
# Create tenure groups
bins = [0, 12, 24, 48, df['tenure'].max()]
labels = ['0–12 months','13–24 months','25–48 months','49+ months']
df['tenure_group'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=True)

plt.figure(figsize=(6,4))
sns.countplot(x='tenure_group', hue='Churn', data=df)
plt.title("Churn by Tenure Group")
plt.ylabel("Number of Customers")
plt.show()

# Churn by Payment Method
plt.figure(figsize=(8,4))
sns.countplot(x='PaymentMethod', hue='Churn', data=df)
plt.title("Churn by Payment Method")
plt.xticks(rotation=45)
plt.ylabel("Number of Customers")
plt.show()
