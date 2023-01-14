class Auto:
    def __init__(self, model, max_speed):
        self.model = model
        self.engine = False
        self.speed = 0
        self.max_speed = max_speed

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print("Silnik odpalony")
        else:
            print("Silnik już był odpalony!")

    def stop_engine(self):
        if self.speed == 0:
            self.speed = False
            print("Silnik zgaszony")
        else:
            print("Najpierw zatrzymaj auto")

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f"Jedziesz z pręskością {self.speed}")
        else:
            print('Odpal najpierw silnik')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f"Jedziesz z pręskością {self.speed}")


bmw = Auto("bmw", 160)
bmw.speed_up(20)
bmw.start_engine()
bmw.speed_up(20)
bmw.speed_up(50)
bmw.speed_up(200)
bmw.stop_engine()
bmw.slow_down(50)
bmw.slow_down(250)
bmw.stop_engine()
