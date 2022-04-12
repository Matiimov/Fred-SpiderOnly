from fredapi import Fred
import pandas as pd
import ssl
from mysql.object import CompanyInfo

ssl._create_default_https_context = ssl._create_unverified_context

fred = Fred(api_key='eed7bc479b25030746c4494763df27d2')

pd.options.display.max_colwidth = 60


companies_info = [('WILL5000INDFC', 'pc1'),('T10Y3M', 'pch'),('T10Y2Y', 'pch'),('HTRUCKSSAAR', 'pc1'),('BAMLH0A3HYCEY', 'pch')]


def is_nan(num):
    return num != num


def parse(company_info):
    data = fred.get_series(company_info[0],
                           observation_start='2012-02-01',
                           observation_end='2022-03-30',
                           units=company_info[1],
                           frequency='m')

    for i in data.items():
        if not is_nan(i[1]):
            CompanyInfo.add(company_info[0], str(i[0].date()), i[1])


for x in companies_info:
    parse(x)