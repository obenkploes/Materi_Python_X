diskon = 20000
jumlah_beli= int(input("Masukkan jumlah beli :"))
bayar = jumlah_beli
# Periksa jumlah pembelian
if(jumlah_beli > 500000):
    bayar = jumlah_beli - diskon
    
# cetak jumlah bayar
print("Jumlah bayar :",bayar)