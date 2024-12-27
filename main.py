import csv
from datetime import date, timedelta


def formatar_texto(txt: str):
    print("="*(len(txt)+2))
    print(" " + txt)
    print("=" * (len(txt) + 2))


def ler_datas(linha: str):
    linha = linha.split(",")
    return linha[1], linha[2], linha[3], linha[4]


duracao_total = 0
dias_permanencia = 0
data_partida_terra = None
data_chegada_destino = None
data_partida_destino = None
data_chegada_terra = None
data_escolha = None

formatar_texto("Voyager Trip - Planejador de Viagens")
print("O que você deseja fazer?\n[1] Ver viagens planejadas\n[2] Planejar viagem")
opcao = int(input("Digite aqui:"))

match opcao:  # calculo da duração da viagem de ida
    case 1:
        print("Nada")
    case 2:
        print("[1] Lua\n[2] Marte\n[3] Europa (Júpiter)")
        destino = int(input("Selecione uma opção"))
        if destino == 2:
            file = open("terra-marte-terra.csv")
            datas = file.readlines()
            c = 1
            for line in datas:
                data = ler_datas(line)
                print(f"[{c}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}"
                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias")
                c += 1
            viagem_escolhida = int(input("Selecione uma das opções de viagem listadas: "))
            print("="*20)
            # Selecionando viagem escolhida pelo usuario
            resumo_viagem = ler_datas(datas[viagem_escolhida - 1])
            print("Viagem escolhida:")  # preciso criar classe viagem
            print(f"Data de início: {resumo_viagem[0]}\n"
                  f"Data de chegada: {resumo_viagem[1]}\n"
                  f"Data de chegada na Terra: {resumo_viagem[2]}\n"
                  f"Dias de viagem no total: {resumo_viagem[3]}")
            formatar_texto("Boa viagem :)")
