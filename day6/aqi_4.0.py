"""
    作者：西西
    版本：4.0
    日期：2019/06/29
    功能：通过BeautifulSoup爬虫获取所有城市数据

"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
    获取城市的AQI
    :param url:
    :return:
    """
    url = 'http://pm25.in/' + city_pinyin
    r=requests.get(url,timeout=30)
    soup=BeautifulSoup(r.text,'lxml')
    div_list=soup.find_all('div',{'class':'span1'})
    city_aqi=[]
    for i in range(8):
        div_content=div_list[i]
        caption=div_content.find('div',{'class':'caption'}).text.strip()
        value=div_content.find('div',{'class':'value'}).text.strip()
        city_aqi.append((caption,value))
    # print(r.status_code)
    return city_aqi


def get_all_cities():
    """
    获取所有城市
    :return:
    """
    url='http://pm25.in/'
    city_list=[]
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div=soup.find_all('div',{'class':'bottom'})[1]
    city_link_list=city_div.find_all('a')
    for city_link in city_link_list:
        city_name=city_link.text
        city_pinyin=city_link['href'][1:]
        city_list.append((city_name,city_pinyin))
    return city_list


def main():
    city_list=get_all_cities()

    for city in city_list:
        city_name=city[0]
        city_pinyin=city[1]
        city_aqi=get_city_aqi(city_pinyin)

        print(city_name,city_aqi)


if __name__ == '__main__':
    main()