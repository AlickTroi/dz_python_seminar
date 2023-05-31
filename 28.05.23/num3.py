# Задача 3. Постройте диаграмму количества студентов 
# заочной формы обучения за 2019 год по всем регионам, 
# в которых общее количество студентов 
# не превышает 10000 за данный год.

import pandas as pd
import seaborn as sns

df = pd.read_csv('https://gbcdn.mrgcdn.ru/uploads/asset/5291776/attachment/817da6a75fe672f89064b6f2bb241a22.csv', sep = ';',encoding='cp1251')
df

df = pd.DataFrame(df, columns=['Численность студентов заочная форма, человек, 2019', 'Субъект РФ'])
df

df = df[df['Численность студентов заочная форма, человек, 2019'] <= 10000]
df

plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов заочная форма, человек, 2019')
plot.set_xticklabels(labels=df['Субъект РФ'], rotation = 90)
plot