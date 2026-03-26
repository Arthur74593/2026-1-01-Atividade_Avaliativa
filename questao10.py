n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
media = float(n1+n2+n3+n4)/4
if media>=6:
    situacao=("aprovado")
    
else:
    situacao=("reprovado")
    
print(f"A média é:{media}\n Situação: {situacao}")

    
