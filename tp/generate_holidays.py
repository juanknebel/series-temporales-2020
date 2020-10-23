import pandas as pd
import numpy as np


# 2016
holidays_2016 = pd.Series([
    '2016-01-01',
    '2016-02-08',
    '2016-02-09',
    '2016-03-24',
    '2016-03-25',
    '2016-04-02',
    '2016-05-01',
    '2016-05-25',
    '2016-06-20',
    '2016-07-08', # puente
    '2016-07-09',
    '2016-07-15', # 17/8
    '2016-10-10', # 12/10
    '2016-12-08', # puente
    '2016-12-09',
    '2016-12-25'
])

# 2017
holidays_2017 = pd.Series([
    '2017-01-01',
    '2017-02-27',
    '2017-02-28',
    '2017-03-27', # 24/3
    '2017-04-02',
    '2017-04-14',
    '2017-05-01',
    '2017-05-25',
    '2017-06-17',
    '2017-06-19', # 20/6
    '2017-07-09',
    '2017-08-21', # 17/8
    '2017-10-09', # 12/10
    '2017-11-27', # 20/11
    '2017-12-08',
    '2017-12-25',
])

# 2018
holidays_2018 = pd.Series([
    '2018-01-01',
    '2018-02-12',
    '2018-02-13',
    '2018-03-24',
    '2018-03-30',
    '2018-04-02',
    '2018-04-30', # puente
    '2018-05-01',
    '2018-05-25',
    '2018-06-20',
    '2018-07-09',
    '2018-08-20',
    '2018-10-15', # 12/10
    '2018-11-19', # 20/11
    '2018-12-08',
    '2018-12-25',
])

# 2019
holidays_2019 = pd.Series([
    '2019-01-01',
    '2019-02-04',
    '2019-02-05',
    '2019-04-02',
    '2019-04-19',
    '2019-05-01',
    '2019-05-25',
    '2019-06-17',
    '2019-06-20',
    '2019-08-08', # puente
    '2019-07-09',
    '2019-08-19', # puente
    '2019-10-14', # 12/10
    '2019-11-18', # 20/11
    '2019-12-08',
    '2019-12-25'
])

# Vacaciones de invierno
#2016 = 18 al 29 de julio
#2017 = 17 al 28 de julio
#2018 = 16 al 27 de julio
#2019 = 22 de julio al 2 de agosto

holidays_winter_2016 = pd.Series(['2016-07-18', '2016-07-29'])
holidays_winter_2017 = pd.Series(['2017-07-17', '2017-07-28'])
holidays_winter_2018 = pd.Series(['2018-07-16', '2018-07-27'])
holidays_winter_2019 = pd.Series(['2019-07-22', '2019-08-02'])

df_holidays = pd.DataFrame({
    'holidays_2016': pd.to_datetime(holidays_2016, format='%Y-%m-%d'),
    'holidays_2017': pd.to_datetime(holidays_2017, format='%Y-%m-%d'),
    'holidays_2018': pd.to_datetime(holidays_2018, format='%Y-%m-%d'),
    'holidays_2019': pd.to_datetime(holidays_2019, format='%Y-%m-%d'),
    'holidays_winter_2016': pd.to_datetime(holidays_winter_2016, format='%Y-%m-%d'),
    'holidays_winter_2017': pd.to_datetime(holidays_winter_2017, format='%Y-%m-%d'),
    'holidays_winter_2018': pd.to_datetime(holidays_winter_2018, format='%Y-%m-%d'),
    'holidays_winter_2019': pd.to_datetime(holidays_winter_2019, format='%Y-%m-%d')
})

df_holidays['dnh_2016'] = df_holidays.holidays_2016.apply(lambda d: d.dayofyear)
df_holidays['dnh_2017'] = df_holidays.holidays_2017.apply(lambda d: d.dayofyear)
df_holidays['dnh_2018'] = df_holidays.holidays_2018.apply(lambda d: d.dayofyear)
df_holidays['dnh_2019'] = df_holidays.holidays_2019.apply(lambda d: d.dayofyear)

df_holidays['dnhw_2016'] = df_holidays.holidays_winter_2016.apply(lambda d: None if pd.isnull(d) else d.dayofyear)
df_holidays['dnhw_2017'] = df_holidays.holidays_winter_2017.apply(lambda d: None if pd.isnull(d) else d.dayofyear)
df_holidays['dnhw_2018'] = df_holidays.holidays_winter_2018.apply(lambda d: None if pd.isnull(d) else d.dayofyear)
df_holidays['dnhw_2019'] = df_holidays.holidays_winter_2019.apply(lambda d: None if pd.isnull(d) else d.dayofyear)

df_holidays.to_csv('./data/holidays.csv', index=False)
