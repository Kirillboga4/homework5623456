import random
class Human:
    def __init__(self, name="Human", job="None", home="None", car="None"):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("Food")
        else:
            self.satiety >=100
            self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("Fuel")
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        def shopping(self, manage):
            if self.car.drive():
                pass
            else:
                self.to_repair()
                return
            if manage == "Fuel":
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                print("Bought food!")
                self.money -= 20
                self.gladness += 10
                self.satiety += 2
        def chill(self):
            self.gladness += 10
            self.home.mess = 0
        def clean_home(self):
            self.gladness -= 5
            self.home.mess = 0
        def to_repair(self):
            self.money -=50
            self.car.strenght = self.car.strenght + 100
        def days_indekses(self, day):
            day = f"Today the {day} of {self.name} `s life"
            print(f"{day:=^50}, \n")
            human_indekses = self.name + "`s indekses"
            print(f"{human_indekses:^50}", "/n")
            print(f"Money - {self.money}")
            print(f"Satiety - {self.satiety}")
            print(f"Gladness - {self.gladness}")
            print(f"{"Homeindekses":^50}", "/n" )
            print(f"Food - {self.home.food}")
            print(f"Mess - {self.home.mess}")
            car_indekses = f"{self.car.brand} car indekses"
            print(f"{car_indekses:^50}", "/n")
            print(f"Fuel - {self.car.fuel}")
            print(f"Strenght - {self.car.strenght}")
        def is_alive(self):
            if self.gladness < 0:
                print ("Depression")
                return  False
            if self.satiety < 0:
                print("Dead...")
            if self.money < -500:
                print("Bankrupt")
                return False
        def live(self, day):
            if self.is_alive() == False:
                return False
            if self.home is None:
                print(f"I bought a car {self.car.brand}")
            if self.job is None:
                self.get_job()
                print(f"I don t have a job, I` m going to get a job{self.job.job}")
            self.days_indekses(day)
            dice = random.randint(1, 4)
            if self.satiety < 20:
                print("I`ll go eat")
                self.eat()
            if self.gladness < 20:
                if self.home.mess > 15:
                    print("I wanna chill, but there is so much mess")
                    self.clean_house()
                else:
                    print("Lets chill")
                    self.chill()
            elif self.money < 0:
                print("Start working!")
                self.work()
            elif self.car.strenght < 15:
                print ("I need to repair  my car")
                self.to_repair()
            elif dice == 1:
                print("Lets chill")
                self.chill()
            elif dice == 2:
                print("Start working")
                self.work()
            elif dice == 3:
                print("Cleaning time")
                self.clean_home()
            elif dice == 4:
                print("Time shopping")
                self.shopping(manage="delecacies")
class auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumptoin = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strenght >0 and self.fuel >= self.consumptoin:
            self.strenght -= 1
            self.fuel -= self.consumptoin
            return False
        else:
            print("The car can` t move!")
            return  False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary =  job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
job_list = {
    "Java developer": {"salary": 50, "gladness": 10},
    "C++ developer": {"salary": 70, "gladness": 20},
    "Python developer": {"salary": 40, "gladness": 50},
    "Rust developer": {"salary": 60, "gladness": 40}
}
brands_of_car = {
    "BMW": {"fuel": 100, "strenght": 100, "consumption": 8},
"LADA": {"fuel": 80, "strenght": 40, "consumption": 12},
"VOLVO": {"fuel": 60, "strenght": 150, "consumption": 6},
"FORD": {"fuel": 50, "strenght": 120, "consumption": 9}
}
nick = Human(name="Nick")
for day in range(1, 8):
    if nick.live(day) == False:
        break
