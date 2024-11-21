import time
import random
class test:
    def __init__(self, lifespan = 1, goober_level = 0, name = None):
        if name == None:
            self.name = "undefined"
            print(f"WARNING! name undefined for {self}")
            time.sleep(3)
        else:  
            self.name = name
        self.lifespan = lifespan
        self.goober_level = goober_level
    def start(self):
        print(f"{self.name} started.")
        while self.lifespan > 0:
            print("                                               ", end= "\r")
            print(f"{self.name} survived with {self.lifespan} lives. Goober level: {self.goober_level}", end= "\r")
            self.goober_level += 1
            self.lifespan += random.randint(-3, 3)
            if self.lifespan > 100:
                self.lifespan += random.randint(-4, 1)
            time.sleep(0.1)
        print("                                                                          ", end= "\r")
        print(f"{self.name} died with goober level {self.goober_level}")
        time.sleep(1)
            
x1 = test(6, 0, "x1")
x2 = test(6, 0, "x2")
x3 = test(7, 0, "x3")

x1.start()
time.sleep(2)
x2.start()
time.sleep(2)
x3.start()

