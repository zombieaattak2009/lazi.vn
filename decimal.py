binary = int(input())
res = [int(x) for x in str(binary)]
tempt = []
tempt2 = 0
mu = len(res)
print(mu)
for elements in res:
    tempt2 = elements**mu
    mu-=1
    tempt.append(tempt2)
print(tempt)