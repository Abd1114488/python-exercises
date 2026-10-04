#An Item is something the player can find, buy or carry
class Item:
    def __init__(self,name,weight,price=0):
        self.name = name
        self.weight = weight
        self.price = price

    # This decides how an item looks when we print it
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"