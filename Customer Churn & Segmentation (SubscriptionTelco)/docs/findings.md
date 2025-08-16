Goal-
Predict customer churn (Yes/No) to identify high-risk customers.

Key Results-
Accuracy: 80.3%
ROC AUC: 0.84 → good separation between churn vs non-churn
Precision (Churn class = 1): 0.65 → when model predicts churn, it’s correct 65% of the time
Recall (Churn class = 1): 0.57 → model catches 57% of actual churners
Confusion Matrix:
True Negatives (loyal customers correctly predicted): 917
False Positives (loyal customers wrongly flagged as churn): 116
False Negatives (missed churners): 161
True Positives (churners correctly predicted): 213

Interpretation-
The model performs better at identifying loyal customers (class 0) than churners.
With an ROC AUC of 0.84, the model has strong discriminatory power.
Business trade-off: Increasing recall (catching more churners) may reduce precision (flagging more loyal customers). Depending on retention campaign costs, we may tune the threshold.

Next Steps-
Try more complex models (Random Forest, XGBoost) to improve recall.
Perform feature importance analysis to identify key churn drivers (e.g., contract type, tenure).
Consider cost-sensitive metrics (e.g., retention campaign ROI) instead of pure accuracy.
