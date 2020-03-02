n = int(input()) #banyak data

if (n>0):
    kolom1 = [] #hutang
    kolom2 = [] #piutang
    kolom3 = [] #jumlah

    for i in range(n):
        data = list(map(int, input().split()))
    
        kolom1.append(data[0])
        kolom2.append(data[1])
        kolom3.append(data[2])

    t = int(input()) #data orang yang dicari

#######################################
    hutang = 0
    piutang = 0
    hutangKpd = []

    for i in range (n):
        if (kolom1[i]==t):
            hutang += kolom3[i]
            hutangKpd.append(kolom2[i])
        if (kolom2[i]==t):
            piutang += kolom3[i]

    print(hutang)
    print(piutang)
    
    hutangKpd.sort()
    print(" ".join(map(str, hutangKpd)), end="")
