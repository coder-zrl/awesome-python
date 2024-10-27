def get_weather_information(city):
    import requests
    import re
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    data={
    'cityname': city,
    'callback': 'success_jsonpCallback',
    '_': '1586315159350'
    }
    url='http://toy1.weather.com.cn/search?'
    response1=requests.get(url,params=data,headers=headers).text
    number=re.findall('"ref":"(\d*?)~',response1)[0]
    weather_url='http://www.weather.com.cn/weather1d/'+number+'.shtml#input'
    response2=requests.get(weather_url,headers=headers).content.decode('utf-8')
    seven_daysdata=re.findall('id="hidden_title" value="(.*?)"',response2)[0].split()
    return ' '.join(seven_daysdata)
