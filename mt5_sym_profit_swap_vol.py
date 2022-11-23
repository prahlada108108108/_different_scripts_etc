import pandas as pd
data1 = pd.read_csv('Deals History.csv',
                   sep='\t',
                   skiprows=1,
                   skipfooter=3,
                   encoding="utf-16")
data = data1.loc[:,['Login','Type', 'Entry','Symbol','Profit','Currency','Volume','Swap']] #+swap(out где) +volume(lots)
#data = data.query("Symbol != '#L-AV'")
instrument_list= ['XAUUSD','GBPUSD','EURUSD','SP500','OIL','USDJPY','NZDUSD','AUDUSD','GBPJPY','GBPCHF','USDCHF','Nd100','DJI','USDCAD','XAGUSD','EURAUD','EURGBP','NZDCAD','EURNZD','EURJPY','GBPAUD','AUDJPY','GBPNZD','AUDNZD','BRN']
data=data[data['Symbol'].isin(instrument_list)]
# print(data.dtypes)
data['Swap'] = data['Swap'].str.replace(' ', '').astype(float)
data['Profit'] = data['Profit'].str.replace(' ', '').astype(float)
data = data.query("Entry == 'out by' or Entry == 'out'")
sym_usd = data.query("Currency == 'USD' ")
sym_jpy = data.query("Currency == 'JPY' ")
sym_eur = data.query("Currency == 'EUR' ")
profit_usd = sym_usd.groupby(('Symbol')).aggregate({'Profit':'sum','Volume':'sum','Swap':'sum'}, axis=1) #swap volume через запятую добавить(?)проверить, в скобочках
profit_jpy = sym_jpy.groupby(('Symbol')).aggregate({'Profit':'sum','Volume':'sum','Swap':'sum'}, axis=1)
profit_eur = sym_eur.groupby(('Symbol')).aggregate({'Profit':'sum','Volume':'sum','Swap':'sum'}, axis=1)

# print(data.dtypes)
#print(type(data['Swap']))
# header = ["InviteTime (Oracle)", "Orig Number", "Orig IP Address", "Dest Number"]
# df.to_csv('output.csv', columns = header)
#header = ['Symbol', 'Profit','Volume','Swap']
profit_eur.to_csv('mt5_eur_res.csv', sep=';')
profit_jpy.to_csv('mt5_jpy_res.csv', sep=';')
profit_usd.to_csv('mt5_usd_res.csv', sep=';')
# profit_eur.to_csv('mt5_eur_res.csv', columns=header)
# profit_jpy.to_csv('mt5_jpy_res.csv', columns=header)
# profit_usd.to_csv('mt5_usd_res.csv', columns=header)
# profit_eur.to_csv('mt5_eur_res.csv', sep=',')
# profit_jpy.to_csv('mt5_jpy_res.csv', sep=',')
# profit_usd.to_csv('mt5_usd_res.csv', sep=',')
print ('JPY', profit_jpy.sort_values(by=['Symbol'], ascending=True),end='\n\n')
print ('EUR', profit_eur.sort_values(by=['Symbol'], ascending=True),end='\n\n')
print ('USD', profit_usd.sort_values(by=['Symbol'], ascending=True),end='\n\n')
#print ('JPY', profit_jpy.sort_values(by=['Profit'], ascending=False))
#print ('EUR', profit_eur.sort_values(by=['Profit'], ascending=False))
#print ('USD', profit_usd.sort_values(by=['Profit'], ascending=False))

# log_profit_jpy = sym_jpy.groupby(('Login')).aggregate({'Profit':'sum'}, axis=1)
# log_profit_usd = sym_usd.groupby(('Login')).aggregate({'Profit':'sum'}, axis=1)
# log_profit_eur = sym_eur.groupby(('Login')).aggregate({'Profit':'sum'}, axis=1)
# log_profit_jpy = log_profit_jpy[log_profit_jpy['Profit'] > 10000]
# log_profit_eur = log_profit_eur[log_profit_eur['Profit'] > 100]
# log_profit_usd = log_profit_usd[log_profit_usd['Profit'] > 100]
# print ('JPY', log_profit_jpy.sort_values(by=['Profit'], ascending=False))
# print ('EUR', log_profit_eur.sort_values(by=['Profit'], ascending=False))
# print ('USD', log_profit_usd.sort_values(by=['Profit'], ascending=False))

#sym_eur.to_csv('test_m.csv', sep=',')
#print (profit_eur)

#сохранить в csv

# list1 =['XAUUSD','GBPUSD','EURUSD','SP500','OIL','USDJPY','NZDUSD','AUDUSD','GBPJPY','GBPCHF','USDCHF','Nd100','DJI','USDCAD','XAGUSD','EURAUD','EURGBP','NZDCAD','EURNZD','EURJPY','GBPAUD','AUDJPY','GBPNZD','AUDNZD','BRN']
#
# OIL
# USDJPY
# NZDUSD
# AUDUSD
# GBPJPY
# GBPCHF
# USDCHF
# Nd100
# DJI
# USDCAD
# XAGUSD
# EURAUD
# EURGBP
# NZDCAD
# EURNZD
# EURJPY
# GBPAUD
# AUDJPY
# GBPNZD
# AUDNZD
# BRN
# '''
