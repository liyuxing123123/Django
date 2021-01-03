#/python3

from distutils.log import warn as printf
from json import dumps
from pprint import pprint

BOOKS = {
    '1':{
        'title':'Core Python Programming',
        'edition':2,
        'year':2007,
    },
    '2':{
        'title':'Python Web Development with Django',
        'authors':['Jeff Forcier', 'Paul Bissex', 'Wesley Chun'],
        'year':2009,
    },
    '3':{
        'title':'Python Fundamentals',
        'year':2009,
    },
}

printf('*** RAW DICT ***')
printf(BOOKS)

printf('\n*** PRETTY_PRINTED DICT ***')
printf(BOOKS)

printf('\n*** RAW JSON ***')
printf(dumps(BOOKS))

printf('\n*** PRETTY_PRINTED JSON ***')
printf(dumps(BOOKS, indent=4))

