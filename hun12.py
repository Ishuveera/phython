try:
    Shh,Ssi=map(int,input().split())
    Ars=list(map(int,input().split()))
    Ars1=sorted(ars)
    print(Ars1[Shh-Ssi])
except ValueError:
    print("invalid")
