def fungsi(angka):
   return angka%5

def insert(angka):
    index = fungsi(angka)
      
    if(tabelHash[index] != 0):
        tabelHash[index] = str(angka) + tabelHash[index]
    else:
        tabelHash[index] = str(angka)

def cetak():
    for i in range(5):
        print(str(i) + "=" + tabelHash[i])

n = int(input())
daftarNim = list(map(int, input().split()))

tabelHash = [0]*5

for nim in daftarNim:
    insert(nim)

cetak()
