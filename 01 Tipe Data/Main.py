

"""
Author : Rin
Discord : Rin#5535
Date : 12/06/2021
"""


#Print "Text"
print("Text")


"""
Tipe Data

Pada python terdapat beberapa tipe data yaitu

    - String
        String merupakan Tipe data dari sekumpulan karakter 
        Contoh : "Saya","Adalah","Rin"

    - Integer
        Integer merupakan Tipe data bilangan bulat
        Contoh : -3,-2,-1,0,1,2,3

    - Float
        Float merupakan Tipe data bilangan desimal
        Contoh : 1.0 | 2.0 | 3.0 | 4.0 | 5.0

    - Boolean
        Boolean merupakan Tipe data bilangan biner dengan parameter True/False | 0 / 1
        Contoh : True, False, 0, 1

untuk lebih lengkapnya bisa di lihat di bawah ini contoh penggunaan Variabel dengan Tipe data
"""

#String
data_string = "Rin"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#Integer
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#Float
data_float = 3.0
print("data : ", data_float)
print("- bertipe : ", type (data_float))

#Boolean
data_bool = False
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

#Tipe data Khusus

#Bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type (data_complex))

#tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type (data_c_double))
