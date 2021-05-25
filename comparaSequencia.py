seq1 = input ("Digite a primeira sequencia (separe os elementos por espaço):")
seq2 = input ("Digite a segunda sequencia (separe os elementos por espaço):")

if seq1==seq2:
    print ("As sequencias sao iguais")
else:
    print ("As sequencias sao diferentes")

count1 = 0
for i in seq2:
    if (i != " "):
        count1 += 1
print("A sequencia 1 tem", count1, "elementos")

count2 = 0
for i in seq2:
    if (i != " "):
        count2 += 1
print("A sequencia 2 tem", count2, "elementos")

