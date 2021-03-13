import pandas as pd
import  numpy as np
df = pd.read_csv('data.csv', encoding='utf-8',dtype=np.str)
symbol_list= df['symbol']
for i in symbol_list:
    print(i)