import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Normalizer


def dt(X_train, X_test, y_train, y_test):
    tree = DecisionTreeClassifier(max_depth=12)
    tree.fit(X_train, y_train)
    predictions = tree.predict(X_test)

    print("Статистика качества прогнозирования:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Точность классификатора(дерево решений): ", accuracy_score(y_test, predictions))

    visualize(y_test, predictions)


def svc(X_train, X_test, y_train, y_test):
    vectors = SVC(kernel='poly', degree=10)
    vectors.fit(X_train, y_train)
    predictions = vectors.predict(X_test)

    print("Статистика качества прогнозирования:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Точность классификатора(метод опорных векторов): ",
          accuracy_score(y_test, predictions))

    visualize(y_test, predictions)


def lr(X_train, X_test, y_train, y_test):
    X_train = Normalizer().fit_transform(X_train)
    X_test = Normalizer().fit_transform(X_test)

    regression = LogisticRegression()
    regression.fit(X_train, y_train)
    predictions = regression.predict(X_test)

    print("Статистика качества прогнозирования:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Точность классификатора(логистическая регрессия): ", accuracy_score(y_test, predictions))

    visualize(y_test, predictions)


def visualize(y_t, y_p):
    test_result = pd.crosstab(index=y_t, columns='result')
    plt.pie(test_result['result'], labels=test_result['result'].index, autopct='%1.1f%%')
    plt.title("Исходные данные")
    plt.show()

    prediction_result = pd.crosstab(index=y_p, columns='result')
    plt.pie(prediction_result['result'], labels=prediction_result['result'].index, autopct='%1.1f%%')
    plt.title("Прогноз")
    plt.show()


# читаем данные
dataset = pd.read_csv('cancer_patient_data_sets.csv')

# получаем информацию о первых строках данных
print(dataset.head())

# размерность набора данных
print("размерность: ", dataset.shape)

# удаляем лишние столбцы
dataset.drop(columns=['index', 'Patient Id'],
             inplace=True)

# получаем набор данных для классификации
X = dataset.drop(columns='Level').values
y = dataset['Level'].values

X_train_main, X_test_main, y_train_main, y_test_main = train_test_split(X, y, test_size=0.3)

print("Метод опорных векторов.")
svc(X_train_main, X_test_main, y_train_main, y_test_main)

print("Дерево решений.")
dt(X_train_main, X_test_main, y_train_main, y_test_main)

print("Логистическая регрессия.")
lr(X_train_main, X_test_main, y_train_main, y_test_main)
