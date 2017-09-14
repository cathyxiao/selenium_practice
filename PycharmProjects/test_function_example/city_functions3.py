#encoding:utf-8
def get_cities(city,country,population=''):
    if population:
    res = city +','+ country + '-' + population
    else
    res = city +','+ country
    return res.title()