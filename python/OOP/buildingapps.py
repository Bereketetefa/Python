class House:
    def __init__(self, numbath, numbedroom):
        #define attributes
        self.numFloors = 2
        self.backyard = 1 
        self.frontyard = 1
        self.kitchen = 1
        self.bathroom = numbath
        self.bedrooms = numbedroom
        self.hasPool = False
        self.numFurniture= 0

    def addPool(self):
        self.hasPool = True

    def addFurnature(self, count):
        self.numFurniture += count


house1 = House (2,3)
house2 = House (1,2)
house3 = House (3,4)

house1.addPool()
house1.addFurnature(5)
house1.addFurnature(2)

house2.addPool()
house2.addFurnature(3)

print(house1.numFurniture)
print(house3.numFurniture)



