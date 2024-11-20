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
            print(f"{self.name} survived with {self.lifespan} lives.")
            self.goober_level += 1
            self.lifespan += random.randint(-3, 3)
            time.sleep(0.2)
        print(f"{self.name} died with goober level {self.goober_level}")
        time.sleep(1)
            
x1 = test(8, 0, "x1")
x2 = test(8, 0, "x2")
x3 = test(8, 0, "x3")

x1.start()
x2.start()
x3.start()

