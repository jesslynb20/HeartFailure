import pandas as pd

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

print("Berikut ini adalah lima data teratas:")
print(df.head())

print("\n Info dataset:")
print(df.info())

#Bagian ini untuk menentukan 5 feature terbaik
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

columns_name = ["age", "anaemia", "creatine_phosphokinase", "diabates", "ejection_fraction", "high_blood_pressure", "platelets", "serum_creatinine", "serum_sodium", "sex", "smoking","time", "DEATH_EVENT"]
array = df.values
X = array[:,0:12]
y = array[:,12]

model = LogisticRegression()
rfe = RFE(model, 5)
fit = rfe.fit(X, y)

print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)

# Bagian ini untuk membagi data train dan data test
from sklearn.model_selection import train_test_split

feature_columns = ["anaemia","ejection_fraction","high_blood_pressure","serum_creatinine","sex"]
X_feature = df[feature_columns]
y = df["DEATH_EVENT"]

X_train, X_test,y_train, y_test = train_test_split(X_feature, y, test_size=0.25, random_state=0)

#Bagian ini untuk melakukan Logistic Regression
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

#Bagian ini untuk memperlihatkan Confusion Matrix
from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
print(cnf_matrix)

#Bagian ini untuk memperlihatkan Confusion Matrix dalam bentuk heat map
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

#Bagian ini untuk memperlihatkan Accuracy, Precision, dan Recall
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))

plt.show()