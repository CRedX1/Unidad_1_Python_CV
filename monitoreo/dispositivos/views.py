from django.shortcuts import render

# Create your views here.
def inicio(request):

    contexto = {"nombre": "Cred"}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "Sensor 2", "valor": 200},
        {"nombre": "Sensor 3", "valor": 300}
    ]
    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
        })

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    consumo_maximo = 100

    # Lista de advertencias y conteo de críticos
    advertencias = []
    estado_critico = 0

    for dispositivo in dispositivos:
        if dispositivo["consumo"] > consumo_maximo:
            advertencias.append(
                f'Advertencia: {dispositivo["nombre"]} supera el límite de consumo ({dispositivo["consumo"]} > {consumo_maximo})'
            )
            estado_critico += 1
        elif dispositivo["consumo"] == consumo_maximo:
            advertencias.append(
                f'Atención: {dispositivo["nombre"]} está justo en el límite de consumo ({consumo_maximo})'
            )

    contexto = {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo,
        "advertencias": advertencias,
        "estado_critico": estado_critico,
    }

    return render(request, "dispositivos/panel.html", contexto)