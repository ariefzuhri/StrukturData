def fungsi(angka):
   return angka%n

def insert(angka):
    index = fungsi(angka)
      
    while (tabelHash[index] != 0):
        index = (index + 1)%n

    tabelHash[index] = angka

def cetak():
    for i in range(n):
        print(str(i) + "=" + str(tabelHash[i]))

n = int(input())
daftarNim = list(map(int, input().split()))

tabelHash = [0]*n

for nim in daftarNim:
    insert(nim)

cetak()
