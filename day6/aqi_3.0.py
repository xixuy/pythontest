"""
    作者：西西
    版本：3.0
    日期：2019/06/29
    功能：通过BeautifulSoup爬虫获取数据

"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city):
    """
    获取城市的AQI
    :param url:
    :return:
    """
    url = 'http://pm25.in/' + city
    r=requests.get(url,timeout=30)
    soup=BeautifulSoup(r.text,'lxml')
    div_list=soup.find_all('div',{'class':'span1'})
    city_aqi=[]
    for i in range(8):
        div_content=div_list[i]
        caption=div_content.find('div',{'class':'caption'}).text.strip()
        value=div_content.find('div',{'class':'value'}).text.strip()
        city_aqi.append((caption,value))
    print(r.status_code)
    return city_aqi


def main():
    city=input('请输入城市拼音：')

    city_aqi=get_city_aqi(city)

    print('空气质量为：{}'.format(city_aqi))


if __name__ == '__main__':
    main()