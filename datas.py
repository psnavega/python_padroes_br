from datetime import datetime, timedelta

class DatasBr():
    def __init__(self, codigo):
        self._momento_cadastro = datetime.now()

    def cadastro(self):
        self.mes_cadastro = self._momento_cadastro.month
        self.ano_cadastro = self._momento_cadastro.year
        self.dia_cadastro = self._momento_cadastro.day
        return self.mes_cadastro

    def seleciona_mes_extenso(self):
        meses_extenso = "janeiro fevereiro marco abril junho julho agosto setembro outubro novembro dezembro".title().split()
        seleciona_mes = meses_extenso[self.cadastro() - 2]
        return seleciona_mes

    def dia_semana(self):
        return self._momento_cadastro.weekday()

    def seleciona_dia_extenso(self):
        dia_extenso = "segunda terca quarta quinta sexta sabado domingo".title().split()
        seleciona_dia_semana = dia_extenso[self.dia_semana()]
        return seleciona_dia_semana

    def formata_data(self):
        data_formatada = self._momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        #Na prática não usaremos TimeDelta porque a data estaria vindo de um banco
        tempo_cadastro = datetime.today() + timedelta(days=30, hours=2) - self._momento_cadastro
        return tempo_cadastro

    def __str__(self):
        return f'{self.seleciona_mes_extenso()} - {self.seleciona_dia_extenso()} - {self.formata_data()} - {self.tempo_cadastro()}'

# FORMAATANDO DATAS
# %A Dias da semana por extenso
# %d Dias do mês (01-31)
# %m Meses em formato de número (01-12)
# %y Ano em formato de 2 dígitos
# %Y Ano em formato de 4 dígitos
# %H Hora no formato decimal (0-23)
# %M Minuto de forma decimal (0-59)
# %S Segundo de forma decimal (0-59)

