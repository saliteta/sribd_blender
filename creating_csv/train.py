import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('coords.csv')
y = df['class'] # target value
X = df.drop('class', axis=1) # features

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

pipelines = {
    'lr':make_pipeline(StandardScaler(), LogisticRegression()),
    'rc':make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf':make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb':make_pipeline(StandardScaler(), GradientBoostingClassifier()),
}

fit_models = {}
for algo, pipeline in pipelines.items():
    model = pipeline.fit(X_train, y_train)
    fit_models[algo] = model

fit_models['rc'].predict(X_test)

