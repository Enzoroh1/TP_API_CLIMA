import requests

def get_clima(ruta, parametros):
    req = requests.get(url=ruta, params=parametros)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = req.json()
        return dic
