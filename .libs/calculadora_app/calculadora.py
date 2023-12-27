import requests
from decouple import config


class CalcularFrete:
    def __init__(self) -> None:
        self.KEY_CORREIO = config("KEY_CORREIO")
        self.KEY_BORZO = config("KEY_BORZO")

    def validar_cep(self, cep):
        CEP_INVALIDO_MSG = "O CEP: {}, é inválido ou não foi encontrado."
        ERRO_VIA_CEP_MSG = "Estamos com um problema para acessar a api do viacep"
        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            response.raise_for_status()
            data = response.json()
            if "erro" in data:
                return {"response_erro": CEP_INVALIDO_MSG.format(cep)}

            return data
        except requests.exceptions.RequestException as error:
            print(f"Erro ao acessar ViaCEP: {error}")
            return {"response_erro": ERRO_VIA_CEP_MSG}
        except Exception as error:
            print(f"Erro ao validar CEP: {error}")
            return {f"{CEP_INVALIDO_MSG}:{error}"}
