import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("wine_quality.csv", sep=',')

print(df.shape)
df.sample(10)

df.info()

df.describe(include='all').T

plt.figure(figsize=(15,9))
# sns.heatmap(df.corr(),cmap='viridis',annot=True)

# get some idea of the data
figure = plt.figure(figsize = (10,6))
# sns.catplot(x="quality", y="fixed acidity", hue="color", kind="swarm", data=df)
plt.title("Wine Quality as explained by Fixed Acidity")


# inspect the relationship between quality and volatile acidity
# sns.catplot(x = 'quality', y = 'volatile acidity', hue="color", kind="swarm", data = df)
plt.title("Wine Quality as explained by Volatile Acidity")


def impute_color(x):
    return 0 if x == 'white' else 1


df['winecolor'] = df['winecolor'].apply(impute_color)

df.value_counts('winecolor')


#Splitting the dataframe into train and test split

# X = df.drop('winecolor',axis=1)
# y = df['winecolor']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# lr = LogisticRegression(class_weight='balanced')
# lr.fit(X_train,y_train)
# y_pred = lr.predict(X_test)
# print(classification_report(y_test,y_pred))

X = df.drop('quality',axis=1)
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = CatBoostRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("Примерный результат предсказания -", y_pred)
print("Средняя абсолютная ошибка -", mean_absolute_error(y_test, y_pred))
print("Средняя квадратичная ошибка -", np.sqrt(mean_squared_error(y_test, y_pred)))
print("Коэффициент детерминации -", r2_score(y_test, y_pred))
print("Предсказание модели -", model.score(X_test, y_test))

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df.to_csv("predicted.csv")

filename = 'model_prediction_quality_wine.sav'
pickle.dump(model, open(filename, 'wb'))
