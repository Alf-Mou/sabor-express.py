notas = [2,4,6,8,10]
tamanho = len(notas)
soma = 0

try:
    for nota in notas:
        soma += nota
        print(nota)
    media = soma / tamanho
    print(media)
except ZeroDivisionError:
    print(f"A lista está vazia")
except Exception as e:
    print(f"A lista possui um erro: {e}")
