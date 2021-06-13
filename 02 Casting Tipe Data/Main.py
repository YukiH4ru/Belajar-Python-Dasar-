"""
Author : Rin
Discord : Rin#5535
Date : 13/06/2021
"""

# Casting Tipe Data
# Merubah dari satu tipe ke tipe lain
# Tipe data = int, float, str, bool

# Data int
print("===[ INT ]===")
data_int = 9;
print("data = ", data_int, ",type =", type(data_int))

# Data int ke float
data_float = float(data_int)
print("data = ", data_float, ",type =",type(data_float))

# Data int ke string
data_string = str(data_int)
print("data = ", data_string, ",type =",type(data_string))

# Data int ke boolean
data_boolean = bool(data_int) #akan bernilai false jika int = 0, dan bernilai true jika nilai int lebih dari 0
print("data = ", data_boolean, ",type =",type(data_boolean))

############################################################

print("===[ FLOAT ]===")
data_float = 9.5;
print("data = ", data_float, ",type =", type(data_float))

# Data float ke int
data_int = int(data_float) # Akan di bulatkan ke bawah
print("data = ", data_int, ",type =",type(data_int))

# Data float ke string
data_string = str(data_float)
print("data = ", data_string, ",type =",type(data_string))

# Data float ke boolean
data_boolean = bool(data_float)
print("data = ", data_boolean, ",type =",type(data_boolean))

############################################################

print("===[ BOOLEAN ]===")
data_boolean = True; # Dapat menggunakan 1 / 0 / True / False
print("data = ", data_boolean, ",type =", type(data_boolean))

# Data boolean ke int
data_int = int(data_boolean)
print("data = ", data_int, ",type =",type(data_int))

# Data boolean ke string
data_string = str(data_boolean)
print("data = ", data_string, ",type =",type(data_string))

# Data boolean ke boolean
data_float = float(data_boolean)
print("data = ", data_float, ",type =",type(data_float))

############################################################

print("===[ STRING ]===")
data_string = "12";
print("data = ", data_string, ",type =", type(data_string))

# Data string ke int
data_int = int(data_string)
print("data = ", data_int, ",type =",type(data_int))

# Data string ke boolean
data_boolean = bool(data_string)
print("data = ", data_boolean, ",type =",type(data_boolean))

# Data string ke float
data_float = float(data_string) #akan bernilai false jika int = 0, dan bernilai true jika nilai int lebih dari 0
print("data = ", data_float, ",type =",type(data_float))

############################################################

