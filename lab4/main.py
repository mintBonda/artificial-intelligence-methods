import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

titles = ['Продукт', 'Сладость', 'Хруст', 'Класс']

food = [['Яблоко', '7', '7', '0'],
        ['Салат', '2', '5', '1'],
        ['Бекон', '1', '2', '2'],
        ['Банан', '9', '1', '0'],
        ['Орехи', '1', '5', '2'],
        ['Рыба', '1', '1', '2'],
        ['Сыр', '1', '1', '2'],
        ['Виноград', '8', '1', '0'],
        ['Морковь', '2', '8', '1'],
        ['Апельсин', '6', '1', '0'],
        ['Ежевика', '9', '1', '0'],
        ['Брокколи', '3', '7', '1'],
        ['Кебаб', '3', '1', '2'],
        ['Айва', '5', '3', '0'],
        ['Свекла', '1', '7', '1']]


def distance(x1, y1, x2, y2):
    return (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5


def knn_method(products, training_size, pars_window, result):
    data = np.array(products)
    test_size = len(data) - training_size
    new_dist = np.zeros((test_size, training_size))
    classes = [0] * test_size
    for i in range(test_size):
        for j in range(training_size):
            dist = distance(int(data[training_size + i][1]), int(data[training_size + i][2]), int(data[j + 1][1]),
                            int(data[j + 1][2]))
            new_dist[i][j] = dist if dist < pars_window else 1000
    for i in range(test_size):
        print(str(i) + ') ' + data[training_size + i][0])
        weights = [0] * products.iloc[:]['Класс'].nunique()
        neighbor = np.sum(new_dist[i] != 1000)
        for j in range(neighbor + 1):
            ind_min = new_dist[i].argmin()
            weights[int(data[ind_min + 1][3])] += ((neighbor - j + 1) / neighbor)
            new_dist[i][ind_min] = 1000
        classes[i] = np.array(weights).argmax()
        print('Спрогнозировнный класс: ', classes[i], 'Настоящий класс: ', data[training_size + i][3])
        if int(classes[i]) != int(data[training_size + i][3]):
            print('нет совпадения')
        else:
            print('совпадение')
            result += 1
    print(classes)
    print('Число совпадений при использовании ручного классификатора составляет', str(result))
    return classes


def knn_sklearn(values, k, y):
    x_train, x_test, y_train, y_test = train_test_split(values, y, test_size=0.30, shuffle=False, stratify=None)

    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    return x_train, x_test, y_train, y_test, predictions


def visualize(data, window, colors):
    x = data['Сладость']
    y = data['Хруст']
    color_list = [colors[str(i)] for i in data['Класс']]
    pylab.subplot(2, 1, window)
    plt.scatter(x, y, c=color_list)
    plt.xlabel('Сладость')
    plt.ylabel('Хруст')


# записывем данные в файл
with open('my_data.csv', 'w', encoding='utf8') as file:
    writer = csv.writer(file, lineterminator="\r")
    writer.writerow(titles)
    for row in food:
        writer.writerow(row)

# чтение набора данных из файла
data = pd.read_csv('my_data.csv')
train = 10
k = 4

X = data.iloc[:, 1:3].values
y = data.iloc[:, 3].values


classes = data[:train]['Класс']

# применение метода knn для первого набора данных
knn_result = pd.Series(knn_method(data, train, 4, 0))
classes = pd.concat([classes, knn_result])

colors = {'0': 'red', '1': 'black', '2': 'blue'}
visualize(data, 1, colors)
colour_list = [colors[str(i)] for i in classes]
plt.show()

# применение метода knn с использованием библиотеки sklearn.
X_train, X_test, y_train, y_test, predictions = knn_sklearn(X, k, y)

# вывод статистики качества прогнозирования
print('Cтатистика качества прогнозирования knn-метода с использованием scikit-learn')
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))


new_food = [['Яблоко', '7', '7', '0'],
            ['Салат', '2', '5', '1'],
            ['Джалеби', '10', '8', '3'],
            ['Бекон', '1', '2', '2'],
            ['Банан', '9', '1', '0'],
            ['Ирис', '10', '9', '3'],
            ['Орехи', '1', '5', '2'],
            ['Рыба', '1', '1', '2'],
            ['Сыр', '1', '1', '2'],
            ['Виноград', '8', '1', '0'],
            ['Леденец', '8', '10', '3'],
            ['Морковь', '2', '8', '1'],
            ['Апельсин', '6', '1', '0'],
            ['Вафли', '6', '9', '3'],
            ['Ежевика', '9', '1', '0'],
            ['Брокколи', '3', '7', '1'],
            ['Халва', '6', '7', '3'],
            ['Кебаб', '3', '1', '2'],
            ['Айва', '5', '3', '0'],
            ['Свекла', '1', '7', '1'],
            ['Шоколад', '7', '8', '3']]

# записываем новые данные в новый файл
with open('new_data.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f, lineterminator="\r")
    writer.writerow(titles)
    for row in new_food:
        writer.writerow(row)

# загрузка нового набора данных
new_data = pd.read_csv('new_data.csv')
train = 14
# применение метода knn для второго набора данных
knn_result = pd.Series(knn_method(new_data, train, k, 0))
start_data = pd.concat([classes, knn_result])

new_X = new_data.iloc[:, 1:3].values
new_y = new_data.iloc[:, 3].values

# применение метода knn с использованием библиотеки sklearn.
X_train, X_test, y_train, y_test, predictions = knn_sklearn(new_X, k, new_y)

# вывод статистики качества прогнозирования
print('Cтатистика качества прогнозирования knn-метода с использованием scikit-learn')
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

colors = {'0': 'red', '1': 'black', '2': 'blue', '3': 'purple'}
visualize(new_data, 1, colors)
plt.show()

