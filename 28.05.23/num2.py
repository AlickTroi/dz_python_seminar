# Задача 2. Постройте диаграмму с данными о 
# численности студентов дневной формы 
# обучения южного федерального округа за 2017 год.

import pandas as pd
import seaborn as sns

df = pd.read_csv('https://gbcdn.mrgcdn.ru/uploads/asset/5291776/attachment/817da6a75fe672f89064b6f2bb241a22.csv', sep = ';',encoding='cp1251')
df

df = df.loc[33:40]
df

sns.barplot(df, x = 'Численность студентов, очная форма, человек, 2017', y = 'Субъект РФ')