alt + shift + ctrl + j - multiple cursors (находит одинаковые слова)
alt + shift + ctrl - multiple cursors (произвольные)
shift + f6 - refactoring (выбираем слово и меняем название всех таких слов)

Virtual Environment (виртуальная среда) -  каталог, в который устанавливаются некоторые исполняемые файлы и скрипты.
Конкретнее она позволяет устанавливать в какой-либо проект библиотеку отдельно от других проектов и глобальной среды.
Пример:
Project1      Project2      Project3  
Django 2      Django 3	    -------- (глобально)

isort - библиотека для сортировки importов.

requirements.txt - файл со всеми библиотеками и их версиями. Полезно для того, чтобы при скидывании кода не было необходимости 
в скидывании виртуальной среды, что может весить очень много. Человек просто скачает себе всё самостоятельно. 
pipenv requirements > requirements.txt
pipenv install -r requirements.txt

pipenv - смесь pip и virtualenv/venv (https://semakin.dev/2020/04/pipenv/).
pip (package installer for Python) — установка и управления зависимостями проекта (пакетный установщик).
env — создание и управление виртуальным окружением для проекта.
pipenv install --skip-lock module_name

****Функции****
def my_func(a: int, b = "123",) -> str:
    pass
b - значение по умолчанию


****Args, Kwargs****
def my_func(*args, **kargs):
    pass

*args - это параметр, который позволяет передавать неопределенное количество позиционных аргументов в функцию. 
Он представляет собой кортеж, содержащий все позиционные аргументы, переданные в функцию.
my_func(1, 2, 3) -> (1, 2, 3)

**kwargs - это параметр, который позволяет передавать неопределенное количество именованных аргументов в функцию. 
Он представляет собой словарь, содержащий все именованные аргументы, переданные в функцию.
my_func(a=1, b=2, c=3) -> {"a": 1, "b": 2, "c": 3}

****lambda функция****
Еще один способ записи функции в питоне - это создание lambda функции. Лямбды функции анонимны, то есть функция безымянна. 
В отличие от def, нам не надо писать название функции. Но мы можем присвоить ее как переменную.

Синтаксис выглядит примерно так:
Lambda аргументы: выражение
f = lambda x: x**2
print(f(2)) -> 4

****Декораторы****

Допустим, нам надо добавить один и тот же функционал для разных функций. Например посчитать время выполнения той или иной функции. 
Вместо того, чтобы переписывать несколько уже существующие функции можно их обернуть в одну новую. Для этого, нам могут и пригодиться декораторы.

Декораторы — это обёртки вокруг Python-функций (или классов), которые изменяют работу того, к чему они применяются. 

Декоратор создается как функция, в параметры которой приходит функция, к которой мы и будем применять декоратор.
Внутри функции декоратора создается функция обертка, внутри которой мы в определенный момент и вызываем функцию, которая передана как аргумент к функции декоратора. 

def decorator_function(func_to_be_called):

    def wrapper(*args, **kwargs):
        print("Some text before calling function")
        func_to_be_called(*args, **kwargs)
        print("Some text after calling function")

    return wrapper

@decorator_function
def print_function(text):
    print("Your text is:", text)

print_function("Hello")

---------------------------------------------
Some text before calling function
Your text is: Hello
Some text after calling function
---------------------------------------------

На одну функцию можно применять несколько декораторов.

from datetime import datetime

def decorator_function(func_to_be_called):
    def wrapper(*args, **kwargs):
        print("Some text before calling function")
        func_to_be_called(*args, **kwargs)
        print("Some text after calling function")
    return wrapper

def time_sum(func):
    def wrapper(text):
        d1 = datetime.now()
        print("Time before calling", d1)
        func(text)
        d2 = datetime.now()
        print("Time after calling", d2)
        print(d2 - d1)
    return wrapper

@time_sum
@decorator_function
def print_function(text):
    print("Your text is:", text)

print_function("Hello")

---------------------------------------------
Time before calling 2023-02-11 16:07:48.526768
Some text before calling function
Your text is: Hello
Some text after calling function
Time after calling 2023-02-11 16:07:48.526843
0:00:00.000075
---------------------------------------------

Иногда, нам необходимо применить декоратор для функции, которая что-то возвращает.
Для этого, при вызове функции в декораторе, результат мы присваиваем переменной и в конце функции обертки возвращаем эту переменную.

def decorator_function(func_to_be_called):
    def wrapper(text):
        print("Some text before calling function")
        result = func_to_be_called(text)
        print("Some text after calling function")
        return result
        
    return wrapper

@decorator_function
def print_function(text):

  return "Your text is: " + text

print(print_function("Hello"))


****Обработка исключений****

Для того, чтобы вывести саму ошибку мы можем ее получать в виде типа Exception
try:
    print(a / b)
except Exception as ex:
    print("Error", ex)

Если нам требуется разные виды ошибок обрабатывать, то можно указать после except и название ошибки, например:
try:
    a, b = map(int, input().split())
    print(a / b)
except ZeroDivisionError:
    print("Error")
except:
    print("Something another")

При обработке исключений можно после блока try использовать блок finally. Он похож на блок except, но команды, написанные внутри него, 
выполняются обязательно. Если в блоке try не возникнет исключения, то блок finally выполнится так же, как и при наличии ошибки, и программа 
возобновит свою работу.
try:
    a, b = int(input()), int(input())
    print(a +b)
except:
    print("error")
finally:
    print("end")

Иногда нужно выполнить определенные действия, когда код внутри блока try не вызвал исключения. Для этого используется блок else.
try:
    a, b = int(input()), int(input())
    print(a + b)
except:
    print("error")
else:
    print("end")

Также мы можем сами вызывать ошибки, для этого используется блок raise.
После raise мы пишем вид ошибки, в аргументах которой вводится комментарий.
a, b = int(input()), int(input())
if a + b == 3:
    raise RuntimeError("Oops, sum is 3")
else:
    print(a + b)

****Классы****
https://proproprogs.ru/python_oop
https://youtube.com/playlist?list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&si=c89wPigXRriSEIP7

В Python, можно сказать, все сущности является объектами. Начиная от переменный и заканчивая классами и функциями.

Переменная x - это объект, точно также как и функция print, и метод find строки. 
Как вы можете заметить, все эти объекты разного типа классов. Таким образом, 
создать класс значит создать новый тип объекта а позже и создать новый экземпляр этого класса.

Для создания класса достаточно написать оператор class и название класса.

class Person:
    pass
Перед вами новый пустой класс Person. Пока что он ничего не делает. Но мы можем создать экземпляр класса.

person_1 = Person()
print(type(person_1), person_1)
<class '__main__.Person'>  <__main__.Person object at 0x00000288CC85B0A0>

Внутри класса могут быть функции, они называются методами.

class Person:
    name = "None" - атрибут класса
    def say_hi():
         print("Hi!")

Person.say_hi()

Если же мы попробуем вызвать функцию у экземпляра, то получим ошибку TypeError.
------------------------------------------------------------------
TypeError: say_hi() takes 0 positional arguments but 1 was given
------------------------------------------------------------------

Дело в том, что когда экземпляр вызывает метод класса, то в аргументах функции он передает самого себя(self).
Поэтому необходимо добавить параметр self в функцию.

class Person:
    name = "default name"
    second_name = "default second name"
    def say_hi(self):
        print("Hi!")
    def set_second_name(self, name):
        second_name = name
Мы можем обратиться к переменной name.

print(person_1.name)
person_1.name = "new name"
print(person_1.name)
----------------
default name
new name
---------------

Переменные name и second_name статические. Доступ к ним можно получить и из самого класса.
Когда мы объявляем переменную внутри класса, но вне метода, она называется статической переменной 
или переменной класса.

Person.name = "new person name"
person_2 = Person()
print(person_2.name, person_1.name, sep=", ")
-------------------------
new person name, new name
-------------------------

Мы создали новый объект person_2, но, так как мы изменили атрибут name у самого класса, то по умолчанию и у новых объектов меняется этот атрибут.

print(person_1.second_name)
person_1.set_second_name("new second name")
print(person_1.second_name)
-------------------
default second name
-------------------

Как видите, изменить статический атрибут внутри объекта нельзя.
Но если мы немного изменим функцию, то мы успешно сможем изменить переменную second_name.

def set_second_name(self, name):
    self.second_name = name

****Конструкторы классов****

В Питоне существуют конструкторы классов. Метод __init__() вызывается каждый раз, когда вы создаете новый объект данного класса.

class Person:
     def __init__(self, name, second_name):
         self.name = name
         self.second_name = second_name

person_1 = Person("Elon", "Musk")

Когда мы создаем объект person_1, у него сразу появляется атрибут name и second_name.
В отличие от других языков программирования, в питоне нельзя создавать несколько конструкторов, поэтому приходится использовать значения по умолчанию.

def __init__(self, name, second_name, age=None):
    self.name = name
    self.second_name = second_name
    self.age = age

person_1 = Person("Elon", "Musk")
person_2 = Person("Bill", "Gates", 67)

****Наследование****

Бывают ситуации, когда некоторые классы могут брать одни те же свойства другого класса. Вместо того, чтобы повторять один и 
тот же код, можно сделать класс, который будет наследовать свойства других классов.

class Person:
    def __init__(self, name, second_name, age =None):
        self.name = name
        self.second_name = second_name
        self.age = age
    def print_name(self):
        print("Your name is", self.name, "\nYour second name is", self.second_name)

class PoliceOfficer(Person):
     Job = "Police department"
При создании второго класса, в скобках мы указали класс который мы наследуем. Наследуются как функции, так и атрибуты. 

person_1 = PoliceOfficer("Chuck", "Noris")

Функция __init__ присутствует у класса Person, значит есть и у класса PoliceOfficer

Мы можем переписать функцию __init__

class PoliceOfficer(Person):
    Job = "Police department"
    def __init__(self, name, second_name, age, has_gun):
         self.name = name
         self.second_name = second_name
         self.age = age
         self.has_hun = has_gun
    def print_info(self):
         print_name()
         print("Your age is", self.age)
         if self.has_gun == True:
            print("You have gun")
         else:

           print("You have not gun")

person_1 = PoliceOfficer("Chuck", "Noris", 67, True)
Мы можем вызвать функцию print_name

person_1.print_name()

--------------------------
Your name is Chuck
Your second name is Noris
--------------------------

Но если мы попробуем вызвать функцию print_name из самого класса, то получим ошибку.

person_1.print_info()

-------------------------------------------
NameError: name 'print_name' is not defined
-------------------------------------------

Для того, чтобы обращаться к функциям класса, который мы наследуем, используется функция super().

    def print_info(self):
         super().print_name()
         print("Your age is", self.age)
         if self.has_gun == True:
            print("You have gun")
         else:
           print("You have not gun")

person_1.print_info()
--------------------------
Your name is Chuck
Your second name is Noris
Your age is 67
You have gun
--------------------------

Таким образом, функцию __init__ можно было бы сократить

class PoliceOfficer(Person):
    Job = "Police department"
    def __init__(self, name, second_name, age, has_gun):
         super().__init__(name, second_name, age)
         self.has_gun = has_gun

attribute (без одного или двух подчеркиваний вначале) – публичное свойство (public);
_attribute (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
__attribute (с двумя подчеркиваниями) – режим доступа private (служит для обращения только внутри класса).

def _my_func():
    pass

__del__(self): - финализатор класса (выполняется перед удалением объекта из памяти)
   pass

from accessify import private, protected 
@private/protected - делают методы РЕАЛЬНО private и protected (к классическим можно получить доступ отовсюда). Нужны только в крайних случаях.

@classmethod - делает метод методом класса (может обращаться к атрибутам класса, но не может обращаться к локальным свойствам экземплярам класса) 
def method_name(cls,...):
    return cls.Data1 and ...
    
@staticmethod - делает метод статичным (не может обращаться ни к атрибутам класса (может, но для этого есть @classmethod),  ни к локальным свойствам экземплярам класса) 
def method_name(...): - нет ни cls, ни self
    return ...

без @classmethod и @staticmethod - может обращаться к атрибутам самого класса и к локальным свойствам экземпляра