# Задача 1. Найдите, какая область 
# центрального федерального округа имела наибольшую 
# численность студентов вечерней формы обучения в 2015 году.

import pandas as pd

df = pd.read_csv('https://gbcdn.mrgcdn.ru/uploads/asset/5291776/attachment/817da6a75fe672f89064b6f2bb241a22.csv', sep = ';',encoding='cp1251')
df

df = pd.DataFrame(df, columns=['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015'])
df

df = df.loc[2:19]
df

df = df.max() 
df