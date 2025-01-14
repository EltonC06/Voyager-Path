from datetime import datetime

from viagem import Viagem
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

duracao_total = 0
dias_permanencia = 0
data_partida_terra = None
data_chegada_destino = None
data_partida_destino = None
data_chegada_terra = None
data_escolha = None

Window.size = (Window.height * 9 / 16, Window.height)


def ler_datas(linha: str):
    linha = linha.split(",")
    return linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]


class Menu(Screen):
    pass


class ViagensPlanejadas(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.datas = open("viagens_reservadas.csv").readlines()
        self.carregar_viagens_planejadas()
        self.contador = None

    def carregar_viagens_planejadas(self):
        cor_fundo_1 = [0, 0.5, 0.5, 1]
        cor_fundo_2 = [0, 0.3, 0.5, 1]
        self.contador = 1
        for linha in self.datas:

            data = ler_datas(linha)
            if self.contador % 2 == 0:
                btn = Button(text=f"[{self.contador}] Destino: {data[0]} Início da viagem: {data[1]}, "
                                  f"Chegada no destino: {data[2]}"
                                  f", Fim da viagem: {data[3]}, Duração total:{data[4]} dias",
                             background_color=cor_fundo_1)
            else:
                btn = Button(text=f"[{self.contador}] Destino: {data[0]} Início da viagem: {data[1]}, "
                                  f"Chegada no destino: {data[2]}"
                                  f", Fim da viagem: {data[3]}, Duração total:{data[4]} dias",
                             background_color=cor_fundo_2)

            self.ids.viagens_reservadas.add_widget(btn)
            self.contador += 1

    pass


class ReservarViagem(Screen):
    def __init__(self, destino: str, **kw):
        super().__init__(**kw)
        self.viagem_escolhida = None
        self.datas = None
        self.destino = destino
        self.contador = 1
        self.carregar_viagem(destino)

    def carregar_viagem(self, destino):
        self.contador = 1
        match destino:
            case "lua":

                print("Lua")
                self.datas = open("terra-lua-terra.csv").readlines()
                for linha in self.datas:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Lua: {data[1]}"
                                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias",
                                 on_press=lambda instance, c=self.contador: self.salvar_viagem("lua", c)
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "marte":
                print("Marte")
                self.datas = open("terra-marte-terra.csv").readlines()
                for linha in self.datas:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}"
                                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias",
                                 on_press=lambda instance, c=self.contador: self.salvar_viagem("marte", c)
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "jupiter":
                print("Jupiter")

                self.datas = open("terra-jupiter-terra.csv").readlines()
                for linha in self.datas:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Jupiter: {data[1]}"
                                      f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias",
                                 on_press=lambda instance, c=self.contador: self.salvar_viagem("jupiter", c)
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

    def salvar_viagem(self, destino: str, num_viagem: int):
        # aqui recebo o destino, para poder abrir o arquivo correto
        # e após isso, o número da linha da viagem que o usuario escolheu
        match destino:  # abrindo arquivo diferente dependendo da viagem que o usuario escolheu
            case "lua":
                print("Lua")
                self.datas = open("terra-lua-terra.csv").readlines()
            case "marte":
                print("Marte")
                self.datas = open("terra-marte-terra.csv").readlines()
            case "jupiter":
                print("Jupiter")
                self.datas = open("terra-jupiter-terra.csv").readlines()

        # Transformando csv formato em uma lista. Criterio de separação: ","
        self.viagem_escolhida = ler_datas(self.datas[num_viagem-1])
        # Convertendo dados da viagem escolhida para a Classe Viagem
        viagem = Viagem(
            self.viagem_escolhida[0],
            converter_str_date(self.viagem_escolhida[1]),
            converter_str_date(self.viagem_escolhida[2]),
            converter_str_date(self.viagem_escolhida[3]),
            int(self.viagem_escolhida[4]),
            float(self.viagem_escolhida[5])
        )
        # salvando viagem escolhida em formato csv
        open("viagens_reservadas.csv", "a").writelines(viagem.converter_csv())
        # Retorno à tela inicial
        app.tela_menu_inicial()

    pass


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None

    def build(self):
        self.sm = ScreenManager()
        # Adicionando telas no objeto ScreenManager
        self.sm.add_widget(Menu(name="Menu"))
        self.sm.add_widget(ViagensPlanejadas(name="ViagensPlanejadas"))
        return self.sm

    def tela_menu_inicial(self):
        self.sm.current = "Menu"

    def tela_menu_viagens_planejadas(self):
        self.sm.current = "ViagensPlanejadas"

    def tela_reservar_viagem(self, destino: str):
        # Criando a tela assim que aperta o botão
        self.sm.add_widget(ReservarViagem(name="ReservarViagem", destino=destino))
        self.sm.current = "ReservarViagem"


def converter_str_date(data_str: str):
    data_convertida = datetime.strptime(data_str, "%b-%d-%Y")
    return data_convertida.date()


if __name__ == '__main__':
    app = MainApp()
    app.run()
