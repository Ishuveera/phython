B,S=map(str,input().split("|"))
C=input()
if  len(B)>len(S):
    if len(B)==len(S)+len(C):
        print(B+"|"+S+C)
elif len(B)<len(S):
     if len(S)==len(B)+len(C):
        print(B+C+"|"+S)
elif len(B)==len(S) and len(C)>1 or (len(S) or len(B)):
    print("impossible")
