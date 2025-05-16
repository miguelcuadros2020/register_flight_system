import re
from fun_using import validation_generic as funval
import datetime as dt

vuelos = {
    "AV-101": {
        "origen": "Lima",
        "destino": "Bogotá",
        "asientos": ["A1", "A2", "B1", "B2"],
        "horario": (dt.datetime(2025,12,4,15,30))
    },
    "AV-201": {
        "origen": "Lima",
        "destino": "Cusco",
        "asientos": ["C1", "C2", "C3", "C4"],
        "horario": (dt(2025, 5, 15, 8, 0), 8, 0, 0, 0)
    },
    "AV-202": {
        "origen": "Bogotá",
        "destino": "Medellín",
        "asientos": ["D1", "D2", "D3"],
        "horario": (dt(2025, 5, 15, 10, 30), 10, 30, 0, 0)
    },
    "AV-203": {
        "origen": "Quito",
        "destino": "Guayaquil",
        "asientos": ["E1", "E2", "E3", "E4", "E5"],
        "horario": (dt(2025, 5, 15, 12, 0), 12, 0, 0, 0)
    },
    "AV-204": {
        "origen": "Santiago",
        "destino": "Valparaíso",
        "asientos": ["F1", "F2"],
        "horario": (dt(2025, 5, 15, 14, 15), 14, 15, 0, 0)
    },
    "AV-205": {
        "origen": "Buenos Aires",
        "destino": "Córdoba",
        "asientos": ["G1", "G2", "G3"],
        "horario": (dt(2025, 5, 15, 16, 45), 16, 45, 0, 0)
    }
}
tickets = {
    1001: {"name": "Juan Pérez", "seats": ["C1", "C2"], "key_flight": "AV-201"},
    1002: {"name": "María Gómez", "seats": ["C3"], "key_flight": "AV-201"},
    1003: {"name": "Carlos López", "seats": ["D1", "D2"], "key_flight": "AV-202"},
    1004: {"name": "Ana Martínez", "seats": ["D3"], "key_flight": "AV-202"},
    1005: {"name": "Pedro Sánchez", "seats": ["E1", "E2", "E3"], "key_flight": "AV-203"},
    1006: {"name": "Laura Ramírez", "seats": ["E4"], "key_flight": "AV-203"},
    1007: {"name": "José Fernández", "seats": ["F1"], "key_flight": "AV-204"},
    1008: {"name": "Sofía Díaz", "seats": ["F2"], "key_flight": "AV-204"},
    1009: {"name": "Miguel Torres", "seats": ["G1", "G2"], "key_flight": "AV-205"},
    1010: {"name": "Lucía Hernández", "seats": ["G3"], "key_flight": "AV-205"}
}

var_1 = [1,2,3,4,5,6,7]
var_2 = [5,6,7]
if var_2 in var_1:
    print("si")
# for x in vuelos.keys():
#     print(vuelos[x]["asientos"] if x in vuelos else print("no se encontro"))
# fuction by creating of the flight
def creating_flight(key:str,origin:str,destini:str,seats:list[str],time:dt.datetime):
    vuelos[key] = {"origen": origin,"destino": destini,"asientos": seats,"horario": (time)}

def tiket_flight(cedula:int,name:str,seats:list[str],key_flight:str):
    tickets[cedula] = {"name":name,"seats":seats,"key_flight":key_flight}

def seats_available(seat, key_vuelo)->bool:
    var_vuelos = vuelos[key_vuelo]
    if seat in var_vuelos["asientos"]:
        for client in tickets.keys():
            var_tikets = tickets[client] 
            if var_tikets["key_flight"] == key_vuelo: 
                if seat in var_tikets["seats"]:
                    return False                  
    else:
        return False
    return True

def percentage_flight():
    result:float = 0

    for seat_count in  vuelos.keys():
        total_seats_tikets = 0
        total_seats_vuelos = len(vuelos[seat_count]["asientos"])
        
        for client in tickets.keys():
                var_tikets = tickets[client]
                if var_tikets["key_flight"] == seat_count :  total_seats_tikets += len(var_tikets["seats"])
                
        result = total_seats_vuelos / total_seats_tikets
        print(f"The flight: {seat_count} is: {(result*100):.2f} occupied.\n")

