###########################[ List Standar ]##########################
list = [["Nomer Absen","Nama","Alamat"],["01","Mamat","Jl.Penguin"]]
print(list[1][0:])


###########################[ List Len ]##########################
my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]

# Tampilkan isi list my_friends dengan nomer indeks 3
print("Isi my_friends indeks ke-3 adalah: {}".format(my_friends[3]))

# Tampilkan semua daftar teman
print("Semua teman: ada {} orang".format(len(my_friends)))
for friend in my_friends:
    print(friend)