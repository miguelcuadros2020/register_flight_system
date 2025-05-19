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
        "horario": dt.datetime(2025,5,15,8,0)
    },
    "AV-202": {
        "origen": "Bogotá",
        "destino": "Medellín",
        "asientos": ["D1", "D2", "D3"],
        "horario": dt.datetime(2025, 5, 15, 10, 30)
    },
    "AV-203": {
        "origen": "Quito",
        "destino": "Guayaquil",
        "asientos": ["E1", "E2", "E3", "E4", "E5"],
        "horario": dt.datetime(2025, 5, 15, 12, 0)
    },
    "AV-204": {
        "origen": "Santiago",
        "destino": "Valparaíso",
        "asientos": ["F1", "F2"],
        "horario": dt.datetime(2025, 5, 15, 14, 15)
    },
    "AV-205": {
        "origen": "Buenos Aires",
        "destino": "Córdoba",
        "asientos": ["G1", "G2", "G3"],
        "horario": dt.datetime(2025, 5, 15, 16, 45)
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

separated = lambda x : [x.strip() for x in x.split(",")]

def main():
    print("welcome!")
    is_alpha = lambda x : x.replace(" ","").isalpha()
    yes_or_no = lambda x : x.lower() == "y" or x.lower() == "n"
    one_leter = lambda x : x.strip().lower()[0]
    separated_valid_seats = lambda x : valid_seats_type(separated(x)) 
    sepatared_valid_flight = lambda x : re.match(r'^[A-Z]{2}-\d{3}$',x)
    flight_user_exist = lambda x : x in vuelos.keys()

    extin_while = True
    while extin_while:

        option_menu = menu()
        match option_menu:
            case 1:
                key:str = funval(str,"Enter the key or the number of the flight: ",[sepatared_valid_flight])
                origine:str = funval(str,"Enter to the origine: ",[is_alpha])
                destiny:str = funval(str,"Enter to the destiny: ",[is_alpha])
                seats:list = separated(funval(str,"Enter the seats to separated by commas: ", [separated_valid_seats]))
                timetable = dt.datetime(funval(dt.datetime,"Enter to the timetable, example (2015-12-4 12:30): ",[lambda x : dt.datetime.strptime(x,"%Y-%m-%d %H:%M")]))

                creating_flight(key, origine, destiny, seats, timetable)
            
            case 2: 
                id_user:int = funval(int,"Enter the id: ")
                name:str = funval(str,"Enter the name: ",[is_alpha])
                key_flight:str = funval(str,"Enter the key or the number of the flight: ",[sepatared_valid_flight,flight_user_exist])

                def seats_available_filtred(seats_list):
                    return seats_available(separated(seats_list) ,key_flight)


                seats:list = separated(funval(str,"Enter the seats to separated by commas: ",[separated_valid_seats,seats_available_filtred]))
                
                tiket_flight(id_user, name, seats, key_flight)
            
            case 3:
                percentage_flight()
            
            case 4:
                tikets_organized()
            
        option_extin = one_leter(funval(str,"do you want to extin?: Yes/No: ",[is_alpha, yes_or_no]))
        if option_extin == "s":
            extin_while = False

def menu():
    print("\n1.) for add a flight.\n" \
          "2.) for add a tiket.\n"\
          "3.) for check the flights.\n"\
          "4.) for check the tiquets.\n"\
          "5.) for extin to the program.\n")
    option = funval(int,"Enter the option: ",[lambda x : 1 <= x <= 5])
    return option

def creating_flight(key:str,origin:str,destiny:str,seats:list[str],time:dt.datetime):
    vuelos[key] = {"origen": origin,"destino": destiny,"asientos": seats,"horario": (time)}

def tiket_flight(id_user:int,name:str,seats:list[str],key_flight:str):
    tickets[id_user] = {"name":name,"seats":seats,"key_flight":key_flight}

def seats_available(seat:list, key_vuelo:str)->bool:
    result:bool = True
    var_vuelos = vuelos[key_vuelo]["asientos"]
    if all(seats in var_vuelos for seats in seat):
        for client in tickets.keys():
            var_tikets = tickets[client] 
            if var_tikets["key_flight"] == key_vuelo: 
                if all(seats in var_tikets["seats"] for seats in seat):
                    result = False 
                    break                 
    else:
        result = False
    return result

def percentage_flight():
    result:float = 0

    for seat_count in  vuelos.keys():
        total_seats_tikets:int = 0
        total_seats_vuelos:int = len(vuelos[seat_count]["asientos"])
        
        for client in tickets.keys():
            var_tikets = tickets[client]
            if var_tikets["key_flight"] == seat_count :  total_seats_tikets += len(var_tikets["seats"])
                
        result = total_seats_tikets / total_seats_vuelos 
        print(f"The flight: {seat_count} is: {(result*100):.2f}% occupied.")



def tikets_organized():
    users_result:list[dict] = []

    for _,inf in tickets.items():
        key_flight:str = inf["key_flight"]
        vuelo:dict = vuelos.get(key_flight)
        timetable:dt.datetime = vuelo["horario"]
        route:list[str] = [vuelo["origen"],vuelo["destino"]]

        users_result.append(
            {"name":inf["name"], 
             "flight":key_flight, 
             "timetable":timetable, 
             "route":route}
             )
    
    users_result.sort(key = lambda x : x["timetable"] if x["timetable"] else dt.datetime.max)
    for user in users_result:
        timetable_print:dt.datetime = user["timetable"].strftime("%y/%m/%d %H:%M") if user["timetable"] else "is not available"

        print(f"user: {user['name']} flight: {user['flight']} timetable: {timetable_print} origine: {user['route'][0]} destiny: {user['route'][1]}")

def valid_seats_type(seats):
    for x in seats:
        print(x)    
    return all(re.match((r'^[A-Z]{1}\d{1}$'),x.strip().upper())for x in seats)

main()