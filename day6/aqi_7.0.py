"""
    作者：西西
    版本：6.0
    日期：2019/07/01
    功能：通过pandas对数据进行清洗和数据可视化

"""
import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def main():
    aqi_data=pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    #数据清洗
    filter_condition=aqi_data['AQI']>0
    clean_data=aqi_data[filter_condition]


    print('AQI最大值：',clean_data['AQI'].max())
    print('AQI最小值：', clean_data['AQI'].min())
    print('AQI平均值：', clean_data['AQI'].mean())

    top50_cities=clean_data.sort_values(by=['AQI']).head(50)
    print('空气质量最好的50个城市：')
    print(top50_cities)

    #数据可视化
    top50_cities.plot(kind='bar',x='city',y='AQI',title='空气质量最好的50个城市',figsize=(20,10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()