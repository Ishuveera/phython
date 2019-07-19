STT,SSS=map(int,input().split())
SSN=0
Li=[]
for X in range(STT):
      Li.append(input())
for X in range(STT):
      for Y in range(SSS-1):
            if(Li[X][Y]!='R' and Li[X][Y+1]!='R'):
                  SSN+=3
            elif(Li[X][Y]!='G' and Li[X][Y+1]!='G'):
                  SSN+=5
print(SSN)
