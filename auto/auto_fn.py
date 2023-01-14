def auto_factory(model, max_speed):
    return {
        'model': model,
        'engine': False,
        'speed': 0,
        'max_speed': max_speed
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print("Silnik odpalony")
    else:
        print("Silnik już był odpalony!")


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
        print("Silnik zgaszony")
    else:
        print("Najpierw zatrzymaj auto")


def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        print(f"Jedziesz z pręskością {car['speed']}")
    else:
        print('Odpal najpierw silnik')


def slow_down(car, amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f"Jedziesz z pręskością {car['speed']}")


bmw = auto_factory('e46', 160)
speed_up(bmw, 20)
start_engine(bmw)
speed_up(bmw, 50)
speed_up(bmw, 200)
stop_engine(bmw)
slow_down(bmw, 50)
slow_down(bmw, 250)
stop_engine(bmw)
