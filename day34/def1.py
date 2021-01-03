#/python3

# def checkgreaternumber(number1, number2):
#     if number1 > number2:
#         print("Greater number is ", number1)
#     else:
#         print("Greater number is ", number2)
#
# checkgreaternumber(2,4)
# checkgreaternumber(3,1)


# def checkgreaternumber(number1, number2):
#     if number1 > number2:
#         return number1
#     else:
#         return number2
#
# print(checkgreaternumber(1,3))
# print(checkgreaternumber(5,2))

# globalval = 6
#
# def checkglobalvalue():
#     global globalval
#     globalval = 10
#     return globalval
#
# def localvariablevalue():
#     global globalval
#     globalval = 8
#     return globalval
#
# def test1():
#     return globalval
#
# print(checkglobalvalue())
# print(globalval)
# print(localvariablevalue())
# print(globalval)
# print(test1())
# print(globalval)



# import sys
#
# print("Total output is ")
# print(int(sys.argv[1]) + int(sys.argv[2]))

import datetime
from threading import Thread

def checksequential():
    for x in range(1,10):
        print(datetime.datetime.now().time())

def checkparallel():
    print(str(datetime.datetime.now().time()) + "\n")

checksequential()
print("\nNow printing parallel threads\n")

threads = []
for x in range(1,10):
    t = Thread(target=checkparallel())
    t.start()
    threads.append(t)

print(threads)
for t in threads:
    t.join()

print(threads)