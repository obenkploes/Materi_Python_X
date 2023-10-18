diskon = 20000
jumlah_beli= int(input("Masukkan jumlah beli :"))

# periksa jumlah beli
if(jumlah_beli>500000):
    bayar= jumlah_beli - diskon
else:
    bayar = jumlah_beli

# cetak bayar
print("Jumlah yang dibayarkan :",bayar)