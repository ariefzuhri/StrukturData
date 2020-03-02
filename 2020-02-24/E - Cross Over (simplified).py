gen1 = input()
gen2 = input()
x = input()

hasil = ""
for i in range(len(x)):
    if (x[i]=='1'):
        hasil += gen2[i]
    else:
        hasil += gen1[i]
        
print(hasil)
