import pandas as pd

dados = {
    "Cliente": ["Cliente"],
    "Serviço": ["3 Vidros"],
    "Valor": [10680]
}

da = pd.DataFrame(dados)

def arq_acessar():
    print(f"\n{da}\n")

def first_lines():
    print(f"\n{da.head()}\n")

def last_lines():
    print(f"\n{da.tail()}")

def valor_total():
    valor_t = da['Valor'].sum()
    print(f"\nValor total: R$ {valor_t}\n")

def valor_medio():
    valor_m = da["Valor"].mean()
    print(f"\nValor médio: R$ {valor_m}\n")

def arq_excel():
    da.to_excel("Serviços.xlsx", index=False)
    da_excel = pd.read_excel("Serviços.xlsx")
    print(f"\n{da_excel}\n")

def menu():
    print("Olá, Chefe Jottap\n")

    while True:
        try:
            print("1- Acessar BD \n2- Primeiras 5 linhas \n3- Últimas 5 linhas " \
            "\n4- Valor total \n5- Valor médio \n6- Arquivo em excel \n7- Sair")
            digite = int(input("Digite: "))

            if digite == 1:
                arq_acessar()
            elif digite == 2:
                first_lines()
            elif digite == 3:
                last_lines()
            elif digite == 4:
                valor_total()
            elif digite == 5:
                valor_medio()
            elif digite == 6:
                arq_excel()
            elif digite == 7:
                print("\nEncerrando programa...\n")
                break
            else:
                print("\nDigite números de 1 a 7\n")
        except ValueError:
            print("\nError: Digite apenas números\n")
menu()