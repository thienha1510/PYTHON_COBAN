a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

MAX = a

if MAX < b:
    MAX = b

if MAX < c:
    MAX = c

print ("Số lớn nhất là " + str(MAX))