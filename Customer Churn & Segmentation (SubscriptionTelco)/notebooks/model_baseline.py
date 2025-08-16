import pandas as pd
 # ...existing code...
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/raw/telco_churn.csv")

# If TotalCharges has missing or blank values, drop them:
df = df[pd.to_numeric(df['TotalCharges'], errors='coerce').notnull()]
df['TotalCharges'] = df['TotalCharges'].astype(float)

# Convert 'Yes'/'No' to binary (already done for some columns)
binary_cols = ['Churn','Partner','Dependents','PhoneService','PaperlessBilling']
for col in binary_cols:
    df[col] = df[col].map({'Yes':1, 'No':0})

# One-hot encode all other categorical columns
categorical_cols = ['gender','MultipleLines','OnlineSecurity','OnlineBackup',
                    'DeviceProtection','TechSupport','StreamingTV','StreamingMovies',
                    'Contract','PaymentMethod','InternetService']

df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)


# Feature scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['tenure','MonthlyCharges','TotalCharges']] = scaler.fit_transform(df[['tenure','MonthlyCharges','TotalCharges']])

# Train-test split
from sklearn.model_selection import train_test_split

X = df.drop(['customerID','Churn'], axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Train size:", X_train.shape, "Test size:", X_test.shape)

# Train a logistic regression model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Train model
model = LogisticRegression(max_iter=1000, solver='liblinear')
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label="ROC Curve (AUC = %0.2f)" % roc_auc_score(y_test, y_prob))
plt.plot([0,1],[0,1],'--', color='grey')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.title("ROC Curve - Logistic Regression")
plt.savefig("ROC Curve - Logistic Regression.png")
plt.show()

# Get feature importance from logistic regression coefficients
coefficients = model.coef_[0]
feature_names = X.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': coefficients
})

# Sort by absolute value of coefficients (strongest impact first)
importance_df['Abs_Coefficient'] = importance_df['Coefficient'].abs()
importance_df = importance_df.sort_values(by='Abs_Coefficient', ascending=False).head(15)

# Plot
plt.figure(figsize=(10,6))
plt.barh(importance_df['Feature'], importance_df['Coefficient'], color='skyblue')
plt.xlabel("Coefficient Value (Impact on Churn)")
plt.title("Top 15 Features - Logistic Regression")
plt.gca().invert_yaxis()
plt.savefig("Top 15 Features - Logistic Regression.png")
plt.show()
