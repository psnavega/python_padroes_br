import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self._numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return resposta
        else:
            return False

    def formata_telefone(self, _numero):
        padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self._numero)
        return f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'

    def __str__(self):
        return self.formata_telefone(self._numero)

