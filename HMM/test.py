import tushare as ts



test_start_date = '2020-01-01'
test_end_date = '2020-11-11'
ts.set_token('bf3f72285496cb21295f4430e4aaa37e5ea816cd545e4fab31dae006')
#查询当前所有正常上市交易的股票列表
pro = ts.pro_api()

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

print(type(data))

data.to_csv('data.csv')
print(data)
# df = pro.daily(ts_code='002415.sz', start_date='20210308', end_date='20210310')
# print(df)
# hist_prices = ts.get_k_data('002415', test_start_date, test_end_date, ktype="D", autype="none")
# print(hist_prices)

# df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20210301', end_date='202110310')
# print(df)