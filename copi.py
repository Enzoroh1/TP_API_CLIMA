from consumo_api import get_clima

print("¿buscar clima de ciudad por nombre?")
print("¿buscar clima de ciudad por coordenadas?")


dato = input("Ingrese una opcion(nombre o coordenadas):")

while (dato == "nombre" or dato == "coordenadas"):
    
    if dato == "nombre":# pronostico actual de la ciudad por nombre
        ciudad = input("Ingrese el nombre de la ciudad ")
        params = {}
        params["q"] = ciudad
        params["appid"] = "331f65799dc902d85364d398b77a88bc"
        params["units"] = "metric"
        url = "https://api.openweathermap.org/data/2.5/weather"
        clima = get_clima(url, params)
        data = (clima["main"])
        print("El clima de la ciudad de", clima["name"], "es: ")
        print(data)
    
    elif dato == "coordenadas":#pronostico actual por coordenadas
        lat = input("Ingresar la latitud: ")
        lon = input("Ingresar la longitud: ")
        params = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "331f65799dc902d85364d398b77a88bc"
        url_coordenadas = "http://api.openweathermap.org/data/2.5/weather"
        clima = get_clima(url_coordenadas, params)
        data = (clima["main"])
        print("El clima de la ciudad de", clima["name"], "es: ")
        print(data)

    print("¿buscar clima de ciudad por nombre?")
    print("¿buscar clima de ciudad por coordenadas?")
    dato = input("Ingrese una opcion:")


print("palabra invalida")
