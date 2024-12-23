from datetime import date, timedelta


def formatar_texto(txt: str):
    print("="*(len(txt)+2))
    print(" " + txt)
    print("=" * (len(txt) + 2))


destino = None
duracao_viagem = 0
duracao_total = 0
dias_permanencia = 0
data_partida_terra = None
data_chegada_destino = None
data_partida_destino = None
data_chegada_terra = None

formatar_texto("Voyager Trip - Planejador de Viagens")
print("O que você deseja fazer?\n[1] Ver viagens planejadas\n[2] Planejar viagem")
opcao = int(input("Digite aqui:"))

match opcao:  # calculo da duração da viagem de ida
    case 1:
        print("Nada")
    case 2:
        print("[1] Lua\n[2] Marte\n[3] Europa (Júpiter)")
        destino = int(input("Selecione uma opção"))
        if destino == 1:
            file = open("duracao_viagens.txt")
            for line in file:
                if "terra_lua" in line:
                    line = line.split("=")
                    duracao_viagem = int(line[1])
                else:
                    pass
        elif destino == 2:
            file = open("duracao_viagens.txt")
            for line in file:
                if "terra_marte" in line:
                    line = line.split("=")
                    duracao_viagem = int(line[1])
        elif destino == 3:
            file = open("duracao_viagens.txt")
            for line in file:
                if "terra_europa" in line:
                    line = line.split("=")
                    duracao_viagem = int(line[1])


print("="*20)
print("Qual data você deseja viajar?")  # aqui será calculada a data que ele chegará no destino
data = input("Digite aqui [dd/MM/yyyy]:")
data = data.split("/")
# registrando data de partida da terra
data_partida_terra = date(int(data[2]), int(data[1]), int(data[0]))
# calculando data de chegada no destino
data_chegada_destino = data_partida_terra + timedelta(duracao_viagem)

# Quantos dias pretende ficar?
print("="*20)
print(f"Quantos dias pretende ficar em {destino}?")
dias_permanencia = int(input("Digite aqui:"))

# calculando data de saída do destino
data_partida_destino = data_chegada_destino + timedelta(10)

# Calculando data de chegada na terra
data_chegada_terra = data_partida_destino + timedelta(duracao_viagem)

# Duração total da viagem
duracao_total = data_chegada_terra - data_chegada_destino

formatar_texto("Resumo da viagem")
print(f"Data de ida: {data_partida_terra}")
print(f"Dias gastos na nave na ida: {data_chegada_destino-data_partida_terra}")
print(f"Data de chegada em {destino}: {data_chegada_destino}")
print(f"Dias gastos no {destino}: {dias_permanencia}")
print(f"Data de saída do destino: {data_partida_destino}")
print(f"Dias gastos na nave na volta: {data_chegada_terra-data_partida_destino}")
print(f"Data de chegada na Terra: {data_chegada_terra}")
print(f"Duração total da viagem em dias: {data_chegada_terra-data_partida_terra}")
