import json


def read_inf(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)


cars = read_inf("Cars.json")
companies = read_inf("Companies.json")
drivers = read_inf("Drivers.json")
sensors = read_inf("Sensors.json")
users = read_inf("Users.json")
wheels = read_inf("Wheels.json")


def get_id_company(company_name):
    return [i.get('ID_company') for i in companies if i.get("Name") == company_name]


def get_id_driver(driver_name):
    return [i.get('ID_user') for i in users if i.get('Full name') == driver_name]


def type_company(id_company, type_):
    drivers_id = [i.get("ID_user") for i in users if
                  i.get("Type") == type_ and int(i.get("Company")) in id_company]
    return drivers_id


def get_inf_users():
    print("Название компании?")
    company_name = input()
    print("Водитель/Владелец?")
    type_ = input()
    id_users = type_company(get_id_company(company_name), type_)
    return ([(i.get("Full name"), i.get("Birthday")) for i in users
             if i.get('Type') == type_ and i.get('ID_user') in id_users])


def get_inf_drivers():
    print("Название компании")
    company_name = input()
    id_users = type_company(get_id_company(company_name), "Водитель")
    list_inf_user = [
        [i.get("ID_driver"), i.get("Breakdown_frequency"), i.get("Type"), i.get("Rating"), i.get("Describe_driver")]
        for i in drivers if i.get('ID_driver') in id_users]
    for j in users:
        for l in list_inf_user:
            if l[0] == j.get("ID_user"):
                l.append(j.get("Full name"))
                l.append(j.get("Birthday"))
                l.pop(0)
    return list_inf_user


def get_car_driver():
    print("Имя водителя")
    name_driver = input()
    id_drivers = get_id_driver(name_driver)
    cars_id = [i.get("Registration_number") for i in cars if i.get("Driver") in id_drivers]
    return cars_id


def all_wheel_car():
    print("Регистрационный номер машины")
    reg_car = int(input())
    car_id = [i.get("ID_wheel") for i in wheels if i.get("Car_number") == reg_car]
    return car_id


def car_wheels_sensors(reg_car):
    sensors_id = [int(i.get("Sensors")) for i in wheels if i.get("Car_number") == reg_car]
    sensors_inf = [(i.get("ID_sensors"), i.get("Type"), i.get("Readings"))
                   for i in sensors if i.get("ID_sensors") in sensors_id]
    return sensors_inf


def all_sensors_car():
    print("Регистрационный номер машины")
    reg_car = int(input())
    car_sensors = [int(i.get("Sensors")) for i in cars if i.get("Registration_number") == reg_car]
    car_sensors_inf = [(i.get("ID_sensors"), i.get("Type"), i.get("Readings"))
                       for i in sensors if i.get("ID_sensors") in car_sensors]
    return car_sensors_inf, car_wheels_sensors(reg_car)


print(all_sensors_car())