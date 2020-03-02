def tabungAtas(S, data):
    S.append(data)

def tabungBawah(S, data):
    S.insert(0, data)

def ambilAtas(S):
    if (not isEmpty(S)):
        S.pop()

def ambilBawah(S):
    if (not isEmpty(S)):
        S.pop(0)

def isEmpty(S):
    return S == []

n = int(input())
celengan = []

if (n>0):
    for i in range(n):
        masukan = list(input().split(" "))
    
        if (masukan[0] == "0"):
            tabungAtas(celengan, int(masukan[1]))
        elif (masukan[0] == "1"):
            tabungBawah(celengan, int(masukan[1]))
        elif (masukan[0] == "2"):
            ambilAtas(celengan)
        elif (masukan[0] == "3"):
            ambilBawah(celengan)

print(sum(celengan))