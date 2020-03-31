from abstract_data_object import AbstractDataObject


class DecryptDTO(AbstractDataObject):

    def __init__(self, numero_casas, token, cifrado, decifrado, resumo_criptografico):
        self.numero_casas: int = numero_casas
        self.token: str = token
        self.cifrado: str = cifrado
        self.decifrado: str = decifrado
        self.resumo_criptografico: str = resumo_criptografico
