cd = 0
cv = 0
ce = 0
cc = 0
ca = 0

#areaconstrucao = int(input("valor area da construcao:"))
#pa = int(input("valor altura:"))
#pl = int(input("valor largura:"))
#pprof = int(input("valor profundidade:"))

#parea = pl*pa
#pv = pa*pl*pprof
#pp = pa*2+pl*2

#print(parea, pv, pp)

def calcPrimo(x):
    cont = 0
    i = 2
    while x>i:
        if x%i==0:
            cont = cont+1
        else:
            cont = cont
        i = i+1
    if cont == 0:
        print(x)
        
