import tushare
data = tushare.get_hist_data("hs300")["close"]
print(data)
n_days = len(data)