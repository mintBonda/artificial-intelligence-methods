import csv
import random
import statistics
import matplotlib.pyplot as plt
import numpy
import pandas as pandas

# Создание набора данных
titles = ["Табельный номер", "Фамилия И.О.", "Пол", "Год рождения", "Год начала работы в компании", "Подразделение",
          "Должность", "Оклад", "Кол-во выполненных проектов"]

male_surnames = ["Некрасов", "Михеев", "Королев", "Белоусов", "Соколов", "Устинов", "Карпов", "Куликов", "Блинов",
                 "Петров"]
female_surnames = ["Васильева", "Иванова", "Морозова", "Медведева", "Соловьёва", "Сидорова", "Михайлова", "Козловская",
                   "Воробьева", "Гурова"]
initials = ["А.", "Б.", "В.", "Г.", "Д.", "Е.", "Ж.", "З.", "И.", "К.", "Л.", "М.", "Н.", "О.", "П.", "Р.", "С.", "Т.",
            "У.", "Ф.", "Э.",
            "Ю.", "Я."]

genders = ["М", "Ж"]

company_divisions = {
    "маркетинг": ["Менеджер по маркетингу", "Интернет-маркетолог"],
    "разработка": ["Разработчик ПО", "Тимлид", "Веб-дизайнер", "Мобильный разработчик", "Бизнес-аналитик", "DevOps"],
    "тестирование": ["Тестировщик", "QA Manager"],
    "HR": ["HR Аналитик", "HR Manager"]
}

data = []
count = random.randint(1000, 1100)

with open("data.csv", "w") as file:
    writer = csv.writer(file, delimiter="|", lineterminator="\n")
    writer.writerow(titles)
    for i in range(1, count + 1):
        gender = genders[random.randint(0, 1)]
        if gender == "M":
            name = random.choice(male_surnames) + " " + random.choice(initials) + random.choice(initials)
        else:
            name = random.choice(female_surnames) + " " + random.choice(initials) + random.choice(initials)
        year_of_birth = random.randint(1975, 1995)
        year_of_joining = random.randint(year_of_birth + random.randint(18, 26), 2022)
        division = random.choice(list(company_divisions.keys()))
        job_title = random.choice(company_divisions[division])

        if year_of_joining < 2015:
            projects = random.randint(8, 12)
            salary = random.randrange(60000, 80000, 5000)
        elif year_of_joining > 2019:
            projects = random.randint(1, 3)
            salary = random.randrange(20000, 40000, 5000)
        else:
            projects = random.randint(4, 7)
            salary = random.randrange(40000, 60000, 5000)

        employee = [i, name, gender, year_of_birth, year_of_joining, division, job_title, salary, projects]

        writer.writerow(employee)

# чтение данных из csv файла

with open("data.csv", "r") as file:
    years_of_birth = []
    salaries = []
    projects = []
    genders = []

    reader = csv.reader(file, delimiter="|", lineterminator="\n")

    headers = next(reader)

    for employee in reader:
        years_of_birth.append(int(employee[3]))
        genders.append(employee[2])
        salaries.append(int(employee[7]))
        projects.append(int(employee[8]))


def process_data_numpy(data_list, column):
    print('-------------Использование numpy-------------')
    print('Столбец: ', column)
    print('Максимальное значение: ',  numpy.max(data_list))
    print('Минимальное значение: ',  numpy.min(data_list))
    print('Математическое ожидание: ',  numpy.mean(data_list))
    print('Стандартное отклонение: ',  numpy.std(data_list))
    print('Дисперсия: ',  numpy.var(data_list))
    print('Медиана: ',  numpy.median(data_list))
    print('Мода: ',  statistics.mode(data_list))


def process_data_pandas(df, column):
    print('----------------Использование pandas--------------')
    print('Столбец: ', column)
    print('Максимальное значение: ', df[column].max())
    print('Минимальное значение: ', df[column].min())
    print('Математическое ожидание: ', df[column].mean())
    print('Стандартное отклонение: ', df[column].std())
    print('Дисперсия: ', df[column].var())
    print('Медиана: ', df[column].median())
    print('Мода: ', df[column].mode())


process_data_numpy(salaries, titles[7])
process_data_numpy(years_of_birth, titles[3])
process_data_numpy(projects, titles[8])

male_employees = numpy.sum(genders.count('М'))
female_employees = numpy.sum(genders.count('Ж'))
print('Пол')
print('Кол-во сотрудников мужского пола: ', male_employees)
print('Кол-во сотрудников женского пола: ', female_employees)

# работа с pandas
dataframe = pandas.read_csv("data.csv", delimiter="|", lineterminator="\r", header=0, index_col=0, encoding="cp1251")
process_data_pandas(dataframe, "Оклад")
process_data_pandas(dataframe, "Год рождения")
process_data_pandas(dataframe, titles[8])

gender = dataframe['Пол']
male_employees_pandas = gender.value_counts()['М']
female_employees_pandas = gender.value_counts()['Ж']
print('Пол')
print('Кол-во сотрудников мужского пола: ', male_employees_pandas)
print('Кол-во сотрудников женского пола: ', female_employees_pandas)

# построение графиков
# Вывод графика зависимости Оклада от года начала работы в компании
graf = dataframe['Подразделение'].hist()
plt.xlabel('Подразделение')
plt.ylabel('Кол-во сотрудников')
plt.xticks(rotation=90)
plt.title('Распределние работников по отделам')
plt.show()

# Вывод графика зависимости Оклада от года начала работы в компании
plt.subplot(2, 2, 2)
plt.xlabel("Количество выполненных проектов")
plt.ylabel("Оклад")
plt.plot(dataframe["Кол-во выполненных проектов"].sort_values(),
         dataframe["Оклад"].sort_values())
plt.show()

# Вывод диаграммы полов в компании
data = [dataframe["Пол"].value_counts()["М"],
        dataframe["Пол"].value_counts()["Ж"]]
plt.pie(data, labels=["М", "Ж"])
plt.title("Круговая диаграмма полов в компании")
plt.ylabel("")
plt.show()
