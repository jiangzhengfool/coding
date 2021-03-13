#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:quincyqiang 
@license: Apache Licence 
@file: en.py 
@time: 2019-05-01 22:27
@description:
"""
import pandas as pd
import numpy as np

lgb = pd.read_csv('output/lgb_0.9221174752906102.csv')
xgb = pd.read_csv('output/xgb_0.9042040369656723.csv')

lgb['p'] = lgb['p'] * 0.2 + xgb['p'] * 0.7
# lgb['p'] = np.round(lgb['p'],2)


lgb.to_csv('output/en37.csv', index=False)
