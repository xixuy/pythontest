"""
    作者：西西
    版本：6.0
    日期：2019/07/01
    功能：通过pandas对数据进行处理

"""
import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    aqi_data=pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    print('AQI最大值：',aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI平均值：', aqi_data['AQI'].mean())

    top10_cities=aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)


if __name__ == '__main__':
    main()