
# try:
#     a , b = 10
#     print(a, b)
#     console.log("nimadir")
# except NameError:
#     print("Xato nomdan foydalanildi")
# except TypeError:
#     print("Nomlashda xato")

# try:
#     a = 10
#     b = 20
#     c = a + b
#     print(c)
#     a = "hello world"
# except NameError:
#     print("Name error chiqdi")
# except SyntaxError:
#     print("Syntax error chiqdi")
# except TypeError:
#     print("Type error chiqdi")
# except:
#     print("Nomalum xato")


# a = input("Son kirit")
# print(type(a))
# if type(a) != "int":
#     raise SyntaxError("Son kiritishing kerak edi")


# son = int(input("Son kiriting: "))
# if son % 2 == 0:
#     print("Ajoyib, bu juft son")
# else:
#     raise TypeError("Toq son kiritding")

# def fizzBuzz(son):
#     try:
#         if son % 3 == 0 and son % 5 == 0:
#             print("Fizz buz")
#         elif son % 3 == 0:
#             print("Fizz")
#         elif son % 5 == 0:
#             print("Buzz")
#         else:
#             raise TypeError("FizzBuzzdan hech biri emas")
#     except TypeError as t:
#         print(t.args)
# fizzBuzz(15)
# fizzBuzz(12)
# fizzBuzz(10)
# fizzBuzz(11)



# try: 
#     print("salom")
#     print(salom)
# except Exception as e:
#     print(e.args)
# finally:
#     print("Hamma vazifa tugadi")

import random as r
imkon = 0
randomSon = r.randint(1, 100)

while True:
    son = int(input("Son kiriting"))

    if(son > randomSon ):
        imkon += 1
        print("Katta son tanladi")
    elif son < randomSon:
        imkon += 1
        print("Kichik son tanladiz")
    else: 
        print("Son topildi")
        break

    if(imkon > 5):
        raise Exception("Imkoniyat tugadi")
    
    
