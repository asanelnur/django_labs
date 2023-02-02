from dataclasses import dataclass


@dataclass
class Person:
    full_name: str
    age: int

    def __str__(self):
        return f'Full name: {self.full_name}, age: {self.age}'


@dataclass
class Driver(Person):
    experience: int

    def __str__(self):
        return super().__str__()+f', experience year: {self.experience}'


@dataclass
class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f'Power: {self.power}, Company: {self.company}'


@dataclass
class Car:
    carClass: str
    engine: Engine
    driver: Driver
    marka: str

    def start(self) -> None:
        print("Поехали!")

    def stop(self) -> None:
        print("Останавливаемся")

    def turnRight(self) -> None:
        print("Поворот направо")

    def turnLeft(self) -> None:
        print("Поворот налево")

    def __str__(self):
        return f'Car class: {self.carClass},   Engine info =>  {self.engine.__str__()}, Driver info =>  {self.driver.__str__()},   Marka is: {self.marka}'


@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self):
        return f'{super().__str__()}, carrying is {self.carrying}'


@dataclass
class SportCar(Car):
    speed: float

    def __str__(self):
        return f'{super().__str__()}, speed is {self.speed}'


driver1 = Driver(full_name="Driver #1", age=20, experience=2)
driver2 = Driver(full_name="Driver #2", age=40, experience=10)

engine1 = Engine(power=1750, company="Nuclear Steam Turbine")
engine2 = Engine(power=1250, company="Union Pacific Big Boy")

sport_car = SportCar(carClass="Sport", engine=engine1, driver=driver1, marka="test1", speed=300)
lorry_car = Lorry(carClass="Lorry", engine=engine2, driver=driver2, marka="test2", carrying=100)

print(sport_car.__str__())
print(lorry_car.__str__())

car = input('Choose a car (1=sport car, 2=lorry car): ')
match car:
    case '1':
        sport_car.start()
        while True:
            command = input("1 = right, 2 = left, 3 = stop\n")
            match command:
                case '1':
                    sport_car.turnRight()
                case '2':
                    sport_car.turnLeft()
                case '3':
                    sport_car.stop()
                    break
    case '2':
        lorry_car.start()
        while True:
            command = input("1 = right, 2 = left, 3 = stop\n")
            match command:
                case '1':
                    lorry_car.turnRight()
                case '2':
                    lorry_car.turnLeft()
                case '3':
                    lorry_car.stop()
                    break


