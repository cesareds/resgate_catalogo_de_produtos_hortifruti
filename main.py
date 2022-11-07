soma = 0.0
opcao = "0"
hortifruti = {"maçã": 3.50,
              "banana": 1.39,
              "alho-poró": 2.99,
              "kiwi": 29.85,
              "cenoura": 6.00}
while True:
    print("sair", hortifruti)
    opcao = input("Escolha uma das opcões acima")
    if opcao== "maçã" or opcao== "banana" or opcao== "alho-poró" or opcao== "kiwi" or opcao== "cenoura":
        soma = soma + hortifruti[opcao]
    else:
        break
print(soma)