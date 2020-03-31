import requests
import string
import hashlib
from decrypt_dto import DecryptDTO
from requests_toolbelt import MultipartEncoder


class Decrypt:

    def __init__(self):
        self.token = "*****************************************"
        self.json_file = "answer.json"
        self.url = "https://api.codenation.dev/v1/challenge/dev-ps/"

    def get_data(self) -> DecryptDTO:
        request = requests.get(self.url + "generate-data?token=" + self.token)

        if request.status_code == 200:
            return DecryptDTO(**request.json()).save(self.json_file)
        else:
            raise Exception("Houve um erro ao buscar os dados para descriptografar")

    def decrypt(self):
        list_letter: list = list(string.ascii_lowercase)
        decrypt_dto: DecryptDTO = self.load()

        for letter in decrypt_dto.cifrado.lower():
            if letter in list_letter:
                index = list_letter.index(letter) - decrypt_dto.numero_casas
                if index < 0:
                    index = list_letter.__len__() - abs(index)
                decrypt_dto.decifrado = decrypt_dto.decifrado + list_letter.__getitem__(index)
            else:
                decrypt_dto.decifrado = decrypt_dto.decifrado + letter
            decrypt_dto.resumo_criptografico = hashlib.sha1(decrypt_dto.decifrado.encode("utf8")).hexdigest()
        decrypt_dto.save(self.json_file)

    def load(self) -> DecryptDTO:
        return DecryptDTO(**DecryptDTO.load(self.json_file))

    def post_result(self):
        multipart_data = MultipartEncoder(
            fields={
                'answer': (self.json_file, open(self.json_file, 'rb'), 'text/plain')
            }
        )
        headers = {'Content-Type': multipart_data.content_type}
        response = requests.post(self.url + "submit-solution?token=" + self.token, data=multipart_data, headers=headers)
        if response.status_code == 200:
            print(response.json())
        else:
            print(response.content)


if __name__ == '__main__':
    decrypt = Decrypt()
    decrypt.get_data()
    decrypt.decrypt()
    decrypt.post_result()
