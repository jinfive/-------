import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib

# 모델 불러오기
loaded_model = joblib.load('decision_tree_model.pkl')
loaded_label_encoder = joblib.load('label_encoder.pkl')

# 예측 예시
sample_scores = np.array([19000, 17100, 19600]).reshape(-1, 1)
sample_pred = loaded_model.predict(sample_scores)
sample_pred_labels = loaded_label_encoder.inverse_transform(sample_pred)

print("Sample Scores:", [19000, 17100, 19600])
print("Predicted Grades:", sample_pred_labels)