#/python3

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

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


books = Element('books')
for isbn, info in BOOKS.items():
    book = SubElement(books, 'book')
    info.setdefault('authors', 'Wesley Chun')
    info.setdefault('edition', 1)
    for key, val in info.items():
        SubElement(book, key).text = ', '.join(str(val).split(':'))

xml = tostring(books)

print('*** RAW XML ***')
print(xml)

print('\n*** PRETTY_PRINTED XML ***')
dom = parseString(xml)
print(dom.toprettyxml(' '))

print('\n*** FLAT STRUCTURE ***')
for elmt in books.getiterator():
    print((elmt.tag), '-', elmt.text)

print('\n*** TITLES ONLY ***')
for book in books.findall('.//title'):
    print(book.text)


