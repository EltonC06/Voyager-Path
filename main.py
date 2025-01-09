from datetime import date, datetime

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

    def __init__(self, **kw):
        super().__init__(**kw)
        self.datas = open("viagens_reservadas.csv").readlines()
        self.carregar_viagens_planejadas()

    pass


class PlanejarViagem(Screen):
    pass


class MarteViagens(Screen):
    def carregar_marte_viagens(self):
        self.contador = 1
        for linha in self.datas:  # para cada linha no arquivo csv, irei criar um botão contendo as infos da viagem
            data = ler_datas(linha)
            btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}"
                              f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias",
                         on_press=lambda instance, c=self.contador: self.salvar_viagem(instance, c)
                         )
            self.ids.viagens_grid.add_widget(btn)
            self.contador += 1

    def salvar_viagem(self, instance, viagemescolhida):
        dados_viagem_escolhida = ler_datas(self.datas[viagemescolhida - 1])
        # Transformando viagem .csv em objeto Viagem
        viagem = Viagem(
            dados_viagem_escolhida[0],
            converter_str_date(dados_viagem_escolhida[1]),
            converter_str_date(dados_viagem_escolhida[2]),
            converter_str_date(dados_viagem_escolhida[3]),
            int(dados_viagem_escolhida[4]),
            float(dados_viagem_escolhida[5])
        )

        # salvando viagem escolhida
        open("viagens_reservadas.csv", "a").writelines(viagem.converter_csv())
        app.tela_menu_inicial(self)


    def __init__(self, **kw):
        super().__init__(**kw)
        self.datas = open("terra-marte-terra.csv").readlines()
        self.carregar_marte_viagens()


class JupiterViagens(Screen):
    def carregar_jupiter_viagens(self):
        self.contador = 1
        for linha in self.datas:  # para cada linha no arquivo csv, irei criar um botão contendo as infos da viagem
            data = ler_datas(linha)
            btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}"
                              f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias",
                         on_press=lambda instance, c=self.contador: self.salvar_viagem(instance, c)
                         )
            self.ids.viagens_grid.add_widget(btn)
            self.contador += 1

    def salvar_viagem(self, instance, viagemescolhida):
        dados_viagem_escolhida = ler_datas(self.datas[viagemescolhida - 1])
        # Transformando viagem .csv em objeto Viagem
        viagem = Viagem(
            dados_viagem_escolhida[0],
            converter_str_date(dados_viagem_escolhida[1]),
            converter_str_date(dados_viagem_escolhida[2]),
            converter_str_date(dados_viagem_escolhida[3]),
            int(dados_viagem_escolhida[4]),
            float(dados_viagem_escolhida[5])
        )

        # salvando viagem escolhida
        open("viagens_reservadas.csv", "a").writelines(viagem.converter_csv())
        app.tela_menu_inicial(self)


    def __init__(self, **kw):
        super().__init__(**kw)
        self.datas = open("terra-jupiter-terra.csv").readlines()
        self.carregar_jupiter_viagens()

    pass


class LuaViagens(Screen):
    def carregar_lua_viagens(self):
        self.contador = 1
        for linha in self.datas:  # para cada linha no arquivo csv, irei criar um botão contendo as infos da viagem
            data = ler_datas(linha)
            btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}"
                              f", Fim da viagem: {data[2]}, Duração total:{data[3]} dias",
                         on_press=lambda instance, c=self.contador: self.salvar_viagem(instance, c)
                         )
            self.ids.viagens_grid.add_widget(btn)
            self.contador += 1

    def salvar_viagem(self, instance, viagemescolhida):
        dados_viagem_escolhida = ler_datas(self.datas[viagemescolhida - 1])
        # Transformando viagem .csv em objeto Viagem
        viagem = Viagem(
            dados_viagem_escolhida[0],
            converter_str_date(dados_viagem_escolhida[1]),
            converter_str_date(dados_viagem_escolhida[2]),
            converter_str_date(dados_viagem_escolhida[3]),
            int(dados_viagem_escolhida[4]),
            float(dados_viagem_escolhida[5])
        )

        # salvando viagem escolhida
        open("viagens_reservadas.csv", "a").writelines(viagem.converter_csv())
        # Retorno à tela inicial
        app.tela_menu_inicial(self)


    def __init__(self, **kw):
        super().__init__(**kw)
        self.datas = open("terra-lua-terra.csv").readlines()
        self.carregar_lua_viagens()

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
        self.sm.add_widget(PlanejarViagem(name="PlanejarViagem"))
        self.sm.add_widget(MarteViagens(name="MarteViagens"))
        self.sm.add_widget(JupiterViagens(name="JupiterViagens"))
        self.sm.add_widget(LuaViagens(name="LuaViagens"))
        return self.sm

    def tela_menu_inicial(self, instance):
        self.sm.current = "Menu"

    def tela_menu_planejar(self, instance):
        self.sm.current = "PlanejarViagem"

    def tela_menu_viagens_planejadas(self, instance):
        self.sm.current = "ViagensPlanejadas"

    def tela_marte_viagens(self, instance):
        self.sm.current = "MarteViagens"

    def tela_jupiter_viagens(self, instance):
        self.sm.current = "JupiterViagens"

    def tela_lua_viagens(self, instance):
        self.sm.current = "LuaViagens"


def converter_str_date(data_str: str):
    data_convertida = datetime.strptime(data_str, "%b-%d-%Y")
    return data_convertida.date()


if __name__ == '__main__':
    app = MainApp()
    app.run()
