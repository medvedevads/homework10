import pandas as pd 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

# Ищем ункальные значения
col = data['whoAmI'].unique()   # ['robot' 'human']
# Создаем новый датафрейм
datasec = pd.DataFrame(0, index = data.index, columns = col)    # 2 колонки, значения только "0"
# Перебираем исходный датафрейм, если по индексу уникальное значение из исходного датафрейма записываем в новый
for i in col:
    datasec.loc[data['whoAmI'] == i, i] = 1     # меняем значения на "1"
print(datasec)

