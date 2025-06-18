# BOOLEAN
from operator import truediv

# 👉 Boolean adalah salah satu tipe data yang ada di dalam bahasa pemrograman Python.
# 👉 Tipe data Boolean merepresentasikan salah satu dari dua nilai logika yaitu True atau False.
# 👉 Fungsi dari Boolean itu sendiri secara umum adalah
#    untuk mengetahui kebenaran dalam suatu ekspresi apakah bernilai True atau False.

# Contoh
is_buying = True
have_outlier = True
is_completed = False

# Boolean operations
# Python telah menyediakan operator Boolean yaitu comparison dan equality.

# Operator Equality
# ==  artinya sama dengan
# !=  artinya tidak sama dengan

nama_tercantum = "Johan"
nama_penerima = "Johan"

# Kita bisa mengeluarkan output dengan dua cara (di Jupyter Notebook)
# Cara 1
print(nama_tercantum == nama_penerima)

# Cara 2 (hanya bisa di Jupyter notebook)
# nama_tercantum == nama_penerima

angka_1 = 0.232
angka_2 = 2.32

print(angka_1 != angka_2)
print(angka_1 == angka_2)

# Exercise
print("nomor ID ")
nomor_id_tiket = "GA0364"
nomor_id_terdaftar ="GA0364"
print(nomor_id_tiket == nomor_id_terdaftar)

# Operator Comparison (<,<=,>,>=)
print("Motor")
motor_alex = 3
motor_raihan = 2

print(motor_alex > motor_raihan)

#jika comparison pada string seperti menyusun pada kamus tapi kebalik
#huruf z>y>x bukan x>y>z
#huruf besar>huruf kecil
print("judul")
judul1 = 'Bersama Awan'
judul2 = 'Bersama Angin'
judul3 = 'bersama Awan'
judul4 = 'Bersama B'

print(judul1 > judul2)
print(judul3 == judul1)
print(judul4 > judul3)
print(judul4 > judul1)

# Exercise
print("IELTS:")
min_ielts = 5.5
nilai_narya = 6
print(nilai_narya >= min_ielts)

print("KAI:")
KA_Gajayana = 455000
KA_Brawijaya = 475000
print(KA_Gajayana != KA_Brawijaya)

print("Data Scientist:")
algoritma1 = 90
algoritma2 = 85
print(algoritma1 > algoritma2)

print("Data Analyst")
penjualanQ1 = 25000000
penjualanQ2 = 20000000
print(penjualanQ1 > penjualanQ2)
print("---------------------------")







