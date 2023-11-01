print("Jenis \t\t Sewa per hari")
print("==============================")
print("A(Majalah)\t Rp 200")
print("B(Novel)\t Rp 150")
print("A(Komik)\t Rp 100")
print("==============================")
buku = input("Pilih buku (A-C) \t:")
hari =int(input("Lama sewa \t\t:"))
if buku =="A":
    total = 200 * hari
elif buku =="B":
    total=150*hari
elif buku=="C":
    total = 100 * hari
else:
    total = 0
print("Total biaya sewa \t:",total)    