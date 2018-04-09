import json
class Pet:

    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.level = 1
        self.xp_req = self.level * 2
        self.xp_rate = self.xp_req - self.xp
        self.x = 0
        self.y = 0
        self.direction = 0

    def eat(self):
        print("Nom Nom Nom...")
        self.xp += 1
        self.levelUp()
        
    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("Yipee!")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + \
               ", xp=" + str(self.xp) + \
               ", level=" + str(self.level) + \
               ", needed-xp=" + str(self.xp_req)+ "]"
    
    def levelUp(self):
        if self.xp >= self.xp_req:
            self.xp -= self.xp_req
            self.level += 1
            self.xp_req = self.level * 2
            print("level up!")
        else:
            print(self.name + " needs " + str(self.xp_req - 1) + " more xp to level up!")
    
pet1 = Pet("Cogbeon")
pet2 = Pet("002")
pet3 = Pet("003")

