def push(dataBaru):
    s.append(dataBaru)
    printStack()
    
def pop():
    if (not isEmpty(s)):
        s.pop()
        printStack()
    else:
        print("ERROR: STACK KOSONG")
    
def isEmpty(stack):
    return stack == []

def powpush(jumlah, dataBaru):
    for i in range(jumlah):
        s.append(dataBaru)
    printStack()

def powpop(jumlah):
    for i in range(jumlah):
        if (not isEmpty(s)):
            s.pop()
        else:
            break
        
    if (not isEmpty(s)):
        printStack()
    else:
        print("ERROR: STACK KOSONG")

def printStack():
    print("[ ", end="")
    for data in s:
        print(str(data) + " ", end="")
    print("]")    

##################################################
n = int(input())
s = []

for i in range(n):
    req = input()
    perintah = req.split(" ")[0]
        
    if (perintah == "PUSH"):
        dataBaru = int(req.split(" ")[1])
        push(dataBaru)
    elif (perintah == "POP"):
        pop()
    elif (perintah == "POWPUSH"):
        dataBaru = int(req.split(" ")[2])
        jumlah = int(req.split(" ")[1])
        powpush(jumlah, dataBaru)
    elif (perintah == "POWPOP"):
        jumlah = int(req.split(" ")[1])
        powpop(jumlah)
