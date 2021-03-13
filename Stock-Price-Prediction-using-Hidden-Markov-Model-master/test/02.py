# coding: utf-8

# In[1]:


from __future__ import print_function
import datetime

import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
import yfinance as yf

import mplfinance as  mpf

# from  mplfinance import quotes_historical_yahoo as quotes_historical_yahoo_ochl

from hmmlearn.hmm import GaussianHMM

print(__doc__)



# In[2]:


quotes = yf.download("INTC", datetime.date(1995, 1, 1), datetime.date(2012, 1, 6))
print(quotes)
quotes_matrix = quotes.reset_index()

# In[12]:


print(quotes)
quotes = np.array(quotes)
for q in quotes:
    open = np.array(q[0])
    close = np.array(q[3])
    volume = np.array(q[5])
    print(open, close, volume)
    # 获取到开盘价 收盘价 和 交易体量

# In[19]:


open = np.array(quotes[:, 0])
close = np.array(quotes[:, 3])
volume = np.array(quotes[:, 5])
print(open)

# In[22]:


x = np.column_stack([close, volume])
print(x)

# In[25]:


# 以上是用numpy获取数据 ，以下是用HMM训练 运行高斯HMM
print("fitting to HMM and decoding ...", end="")
# 创建一个HMM实例并执行fit
model = GaussianHMM(n_components=4, covariance_type="diag", n_iter=1000).fit(x)

# In[26]:


# 预测内部隐藏状态的最佳顺序
hidden_states = model.predict(x)

# In[27]:


# 以下是画图
print("Transition matrix")
print(model.transmat_)

# In[28]:


print("Means and vars of each hidden state")
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("val = ", np.diag(model.covars_[i]))
    print()

# In[30]:


fig, axs = plt.subplots(model.n_components, sharex=True, sharey=True)
colours = cm.rainbow(np.linspace(0, 1, model.n_components))
# plt.subplots  有s和没有s  有差别的


# In[34]:


for i, (ax, colour) in enumerate(zip(axs, colours)):
    # 使用花哨索引来绘制每个状态的数据
    mask = hidden_states == i
    ax.plot_date(open[mask], close[mask], ".-", c=colour)
    ax.set_title("{0}th hidden state".format(i))
    # Format the ticks.
    ax.xaxis.set_major_locator(YearLocator())
    ax.xaxis.set_minor_locator(MonthLocator())

    ax.grid(True)
plt.show()