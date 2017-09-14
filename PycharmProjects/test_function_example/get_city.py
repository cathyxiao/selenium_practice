#encoding:utf-8
from city_functions import get_cities
print 'user input '
city = raw_input('please input your city: ')
country = raw_input('please input your country: ')
#raw_input函数会将用户输入转化为字符串，而input不会
city_country = get_cities(city,country)
print city_country