def isEmpty():
    return kode == []

n = int(input())

kode = []
judul = []

for i in range(n):
    masukan = list(input().split())
    
    if (masukan[0] == "T"):
        kode.append(masukan[1])
        judul.append(masukan[2])
    elif (not isEmpty() and masukan[0] == "A"):
        kode.pop()
        judul.pop()

for i in range(len(kode)):
    print(kode.pop(), judul.pop())
