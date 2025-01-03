from datetime import date, datetime
from viagem import Viagem
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

duracao_total = 0
dias_permanencia = 0
data_partida_terra = None
data_chegada_destino = None
data_partida_destino = None
data_chegada_terra = None
data_escolha = None


class Menu(Screen):
    pass

class ViagensPlanejadas(Screen):
    pass

class PlanejarViagem(Screen):
    pass


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Menu(name="Menu"))
        self.sm.add_widget(ViagensPlanejadas(name="ViagensPlanejadas"))
        self.sm.add_widget(PlanejarViagem(name="PlanejarViagem"))
        return self.sm

    def trocar_menu_planejar(self, instance):
        self.sm.current = "PlanejarViagem"

    def trocar_menu_viagens_planejadas(self, instance):
        self.sm.current = "ViagensPlanejadas"


def formatar_texto(txt: str):
    print("=" * (len(txt) + 2))
    print(" " + txt)
    print("=" * (len(txt) + 2))


def ler_datas(linha: str):
    linha = linha.split(",")
    return linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]


def converter_str_date(data_str: str):
    data_convertida = datetime.strptime(data_str, "%b-%d-%Y")
    return data_convertida.date()




formatar_texto("Voyager Trip - Planejador de Viagens")
print("O que você deseja fazer?\n[1] Ver viagens planejadas\n[2] Planejar viagem")
opcao = int(input("Digite aqui:"))

match opcao:  # calculo da duração da viagem de ida
    case 1:  # salvar viagem
        viagens_reservadas = []  # viagens salvas serão armazenadas nessa lista, para depois eu pecorre-la
        file = open("viagens_reservadas.csv").readlines()
        print("Viagens reservadas:")
        if len(file) < 1:
            print("Nenhuma viagem reservada até o momento")
        else:
            for viagem in file:
                viagem = ler_datas(viagem)
                v = Viagem(
                    viagem[0],
                    datetime.strptime(viagem[1], "%Y-%m-%d"),  # formatando data (data chega assim: 2025-01-12)
                    datetime.strptime(viagem[2], "%Y-%m-%d"),
                    datetime.strptime(viagem[3], "%Y-%m-%d"),
                    int(viagem[4]),
                    float(viagem[5])
                )
                viagens_reservadas.append(v)
            # Mostrar viagens salvas (falta metodo __str__)
            for viagem in viagens_reservadas:
                print(viagem.__str__())
                print("="*20)

    case 2:
        print("[1] Lua\n[2] Marte\n[3] Júpiter")
        destino = int(input("Selecione uma opção"))

        if destino == 1:
            datas = open("terra-lua-terra.csv").readlines()
            c = 1
            for line in datas:
                data = ler_datas(line)
                print(f"[{c}] Início da viagem: {data[0]}, Chegada na Lua: {data[1]}"
                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias")
                c += 1
            viagem_escolhida = int(input("Selecione uma das opções de viagem listadas: "))
            print("=" * 20)
            print("Viagem escolhida")
            dados_viagem_escolhida = ler_datas(datas[viagem_escolhida-1])
            # Transformando viagem .csv em objeto Viagem
            viagem = Viagem(
                            dados_viagem_escolhida[0],
                            converter_str_date(dados_viagem_escolhida[1]),
                            converter_str_date(dados_viagem_escolhida[2]),
                            converter_str_date(dados_viagem_escolhida[3]),
                            int(dados_viagem_escolhida[4]),
                            float(dados_viagem_escolhida[5])
                            )
            # Armazenamento
            armazenamento = open("viagens_reservadas.csv", "a").writelines(
                [viagem.destino + "," + str(viagem.data_inicio) + "," + str(viagem.data_chegada_destino) + "," +
                 str(viagem.data_chegada_retorno) + "," + str(viagem.duracao) + "," + str(viagem.delta_v) + ",\n"]
            )
            formatar_texto("Boa viagem :)")

        elif destino == 2:
            datas = open("terra-marte-terra.csv").readlines()
            c = 1
            for line in datas:
                data = ler_datas(line)
                print(f"[{c}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}"
                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias")
                c += 1
            viagem_escolhida = int(input("Selecione uma das opções de viagem listadas: "))
            print("=" * 20)
            dados_viagem_escolhida = ler_datas(datas[viagem_escolhida-1])
            # Transformando viagem .csv em objeto Viagem
            viagem = Viagem(
                            dados_viagem_escolhida[0],
                            converter_str_date(dados_viagem_escolhida[1]),
                            converter_str_date(dados_viagem_escolhida[2]),
                            converter_str_date(dados_viagem_escolhida[3]),
                            int(dados_viagem_escolhida[4]),
                            float(dados_viagem_escolhida[5])
                            )
            # Armazenamento
            armazenamento = open("viagens_reservadas.csv", "a").writelines(
                [viagem.destino + "," + str(viagem.data_inicio) + "," + str(viagem.data_chegada_destino) + "," +
                 str(viagem.data_chegada_retorno) + "," + str(viagem.duracao) + "," + str(viagem.delta_v) + ",\n"]
            )
            formatar_texto("Boa viagem :)")

        elif destino == 3:
            datas = open("terra-jupiter-terra.csv").readlines()
            c = 1
            for line in datas:
                data = ler_datas(line)
                print(f"[{c}] Início da viagem: {data[0]}, Chegada em Jupiter: {data[1]}"
                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias")
                c += 1
            viagem_escolhida = int(input("Selecione uma das opções de viagem listadas: "))
            print("=" * 20)
            dados_viagem_escolhida = ler_datas(datas[viagem_escolhida-1])
            # Transformando viagem .csv em objeto Viagem
            viagem = Viagem(
                            dados_viagem_escolhida[0],
                            converter_str_date(dados_viagem_escolhida[1]),
                            converter_str_date(dados_viagem_escolhida[2]),
                            converter_str_date(dados_viagem_escolhida[3]),
                            int(dados_viagem_escolhida[4]),
                            float(dados_viagem_escolhida[5])
                            )
            # Armazenamento
            armazenamento = open("viagens_reservadas.csv", "a").writelines(
                [viagem.destino + "," + str(viagem.data_inicio) + "," + str(viagem.data_chegada_destino) + "," +
                 str(viagem.data_chegada_retorno) + "," + str(viagem.duracao) + "," + str(viagem.delta_v) + ",\n"]
            )
            print("Viagem escolhida")
            formatar_texto("Boa viagem :)")

if __name__ == '__main__':
    app = MainApp()
    app.run()
