#encoding:utf-8
def get_cities(city,country,population=''):
    res = city +','+ country + '-' + population
    return res.title()
#增加一个可空的参数，可空参数前有个符号