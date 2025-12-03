import pandas as pd
import numpy as np
c = 0
df = pd.read_csv('tested.csv')
print('базовые характеристики')
print(df.describe())
print('')
print('количество пустых строк и нулей')
print(sum(df.isna().sum()))
print('')
print('какая информация, в каком столбце')
print(df.info())
print('')
print('количество строк')
print(len(df))
print('')
print('количество столбцов')
print(len(df.columns))
print('')
print("Базовая статистика по стоимости ('Fare'):")
fare = df['Fare']
print("Среднее значение: ", fare.mean())
print("Медиана: ", fare.median())
print("Максимум: ", fare.max())
print("Минимум: ", fare.min())
print("Сумма: ", fare.sum())
print("Количество пропусков: ", fare.isnull().sum())

# Сохраняем строки, где был пропуск в "Fare"
missing_fare = df[df['Fare'].isnull()].copy()

# Заполняем пропуски по среднему значению от класса пассажира с пропуском в 'Fare'
df['Fare'] = df.groupby('Pclass')['Fare'].transform(lambda x: x.fillna(x.mean()))

# Получаем индексы пустых строк
missing_indices = missing_fare.index

# Выводим обновлённые строки
print("Строки, где 'Fare' был пропуском:")
print(df.loc[missing_indices])

print('Пропусков в Age:', df['Age'].isnull().sum())

# Находим наиболее частое значение(Моду) для Age
age_mode = df['Age'].mode()[0]

# Заполняем пропуски
df['Age'] = df['Age'].fillna(age_mode)

print('Используемое значение моды для Age:', age_mode)

# Находим выживших
survived = df[df['Survived'] == 1]
survived_men = survived[survived['Sex'] == 'male']
survived_women = survived[survived['Sex'] == 'female']
total_survived = len(survived)

percent_men = len(survived_men) / total_survived * 100
percent_women = len(survived_women) / total_survived * 100

print("Процент выживших мужчин: ", percent_men)
print("Процент выживших женщин: ", percent_women)

mean_age_men = np.mean(survived_men['Age'])
mean_age_women = np.mean(survived_women['Age'])

print("Средний возраст среди выживших мужчин: ", mean_age_men)
print("Средний возраст среди выживших женщин: ", mean_age_women)

print('')

filtered = df[(df['Sex'] == 'male') & (df['Age'] > 30) & (df['Pclass'] == 1)]
print('Мужчины старше 30, первый класс')
print(filtered)
print('Количество таких пассажиров:', len(filtered))

print('')

filtered = df[((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)]
print('Моложе 18 лет или женщина, и выжили')
print(filtered)
print('Количество таких пассажиров:', len(filtered))

print('')

groups = df.groupby(['Pclass', 'Sex'])
result = groups.agg(mean_age=('Age', 'mean'), survival_rate=('Survived', 'mean'), mean_fare=('Fare', 'mean'))
result['survival_rate'] = result['survival_rate'] * 100
print('Группировка по классу и полу')
print(result)