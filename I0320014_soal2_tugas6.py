data = int(input("Banyaknya data: "))
m = 0
n = 1
while n <= data:
    nilai = float(input("Masukan Nilai ke-%d: "%n))
    m += nilai
    n+=1
rerata = m/data
print("Nilai Rata-Rata: %0.2f" % rerata)