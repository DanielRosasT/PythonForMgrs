## Encuentre la raiz cúbica de un perfecto cubo
ans=0
x= int(input(" ingrese un número entero\n para calcular si es un perfecto cubo ---> "))
while ans**3 < abs(x):
    ans=ans+1
if ans**3 != abs(x):
    print (" no es un cubo perfecto")
    ans = ans-1
    while ans**3 < abs(x):
        ans=ans+ 0.0000001
    print ("la raiz cubica de",x, "es", ans)
else:
    if x < 0:
        ans= -ans
    print ("la raiz cubica de",x, "es", ans)    
print ("\n\n ---------- fin -------------")
