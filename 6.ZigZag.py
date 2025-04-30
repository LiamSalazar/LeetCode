# 0   4   8    12
# 1 3 5 7 9 11 13
# 2   6   10

# 0    6      12
# 1  5 7   11 13
# 2 4  8 10
# 3    9 

# 0     8         16
# 1   7 9      15 17
# 2  6  10   14   18
# 3 5   11 13     19
# 4     12        20

# 0      10          20
# 1    9 11       19 21 
# 2   8  12     18   22
# 3  7   13   17     23
# 4 6    14 16       24
# 5      15          25

# 1) Inicia i=0 Adición=n + n-2
# 2) Inicia i=1 Adición=n-(i+1) + n-(i+1)
# 3) Inicia i=4 Adición=n-(i+1)

# Reglas:
# 1. Si n es impar la fila del centro cumple siempre la regla
# 2. Mitad superior cumple 2)
# 3. Mitad inferior cumple 3)
# 4. Primer y ultima fila cumplen 1
# 5. Cambio de fila cuando el algotimo devuelve un indice mayor al de la longitud de la cadena