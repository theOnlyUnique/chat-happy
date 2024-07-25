from itertools import  permutations
sum = 0
for i in permutations("1234",3)
    print("".join(i))
    sum+=1

print(sum)