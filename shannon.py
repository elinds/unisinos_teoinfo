'''
Teoria da Informacao - UNISINOS - 2020
Analise de frequencias e Shannon
Ernesto Lindstaedt
'''

import math

total = 0;
cntr = [0] * 256
fileName = input("File?")

with open(fileName, "rb") as file:
    while (byte := file.read(1)):
        cntr[ord(byte)] += 1
        total += 1

print("File with ", total, "bytes.")

# Shannon entropy
h = 0.0
for i in range(256):
    if cntr[i] > 0:
        h += ((cntr[i] / total) * (math.log2(cntr[i] / total)))
print("\nShannon entropy H = ", -h, " bits/symbol")

with open(fileName + ".shannon.txt", "w") as file2write:
    for i in range(256):
        file2write.write(str(i) + " " + str(cntr[i]) + " " + chr(i) + '\n')
