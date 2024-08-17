def seculoDoAno(ano):
    if ano % 100 == 0:
        return ano // 100
    else:
        return ano // 100 + 1

# Exemplos de uso
ano1 = 1905
ano2 = 1700

print(f"O século do ano {ano1} é {seculoDoAno(ano1)}")
print(f"O século do ano {ano2} é {seculoDoAno(ano2)}")
