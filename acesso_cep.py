import requests

class CEP:
    def __init__(self, codigo):
        codigo = str(codigo)
        if self.valida(codigo):
            self.cep = codigo
        else:
            raise ValueError("CEP inválido")

    def valida(self, codigo):
        if len(codigo) == 8:
            return True
        else:
            return False

    def busca(self):
        #metodo text retorna uma string - metodo json retorna um dicionario
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

    def formata(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def __str__(self):
        return self.busca()

