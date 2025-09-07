name = "Alexandr"
age = 24
height = 64
print("Имя - ", name)
print("Возраст -", age)
print("Вес - ", height)
x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))
print(x)
a = 7
b = a
print(a)
print(b)
a = 10
print(b, "Значение не изменилось, так как на стр 18 b зафиксировало значение a (на тот момент 7), а мы не меняли после этого значение b")
x, y, z = 100,100,100
print(x,y,z)
print(id(x))
print(id(y))
print(id(z))
x, y, z = 100, 101, 102
print(x,y,z)
print(id(x))
print(id(y))
print(id(z))
print("Разные")
a = 5
b = 10
a,b = 10, 5
print(a,b)
import keyword
print("Переменные нельзя так называть, так как они специально зарезервированы")
print(keyword.kwlist)
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1 = "Проверка"
print(type(var1))
lastname = "Ivanov"
dog_name = "Sharik"
author = "Esenin"
Float = 8.14
count = 0
print(lastname,type(lastname))
print(dog_name,type(dog_name))
print(author,type(author))
print(Float,type(Float))
print(count,type(count))
знач = 10
print(знач)
print("Да, работает")
