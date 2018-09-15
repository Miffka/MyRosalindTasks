# put your python code here
#-*-coding:utf8;-*-
#qpy:3
#qpy:console

word1 = input()
word2 = input()
n, m = map(len, [word1, word2])

#print(n, m)

D = [[0 for i in range(n+1)] for j in range(m+1)]

#print(D)

#for j in range(m+1):
#    print(j)
#    print(D[j])

for i in range(n+1):
    D[0][i] = i

for j in range(m+1):
    D[j][0] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        c = int(word1[i-1]!=word2[j-1])
#        print(word1[i-1], word2[j-1], c)
        D[j][i] = min(D[j-1][i]+1, D[j][i-1]+1, D[j-1][i-1]+c)

#for j in range(m+1):
#    print(D[j])

#print(n, m)
print(D[m][n])

