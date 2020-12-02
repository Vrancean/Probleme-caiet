n=input("introdu un cuvîntul:")
m=input("introdu o oarecare literă:")
for i in range(len(n)):
    print(n[:i]+m+n[i+1:])