def push(T, data):
    m = len(T)
    T.insert(int(m/2), data)
        
n = int(input())
data = list(input().split())
T = []

for i in range(n):
    push(T, data[i])

for i in range(n):
    print(T[i], end=" ")
print()
