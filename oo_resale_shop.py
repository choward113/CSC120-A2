from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def buy(self, computer):
        #Adds computer to inventory
        self.inventory.append(computer)

    def sell(self, computer):
        #Removes computer from inventory
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Computer not found")
    
    def print_inventory(self):
        # Prints each computer's details if the inventory is not empty.
        if self.inventory: 
            for computer in self.inventory:
                print("Description:",computer.description,
                "\nProcessor Type:", computer.processor_type,
                "\nHard Drive Capacity:", computer.hard_drive_capacity,
                "\nMemory:", computer.memory,
                "\nOperating System:", computer.operating_system,
                "\nYear Made:", computer.year_made,
                "\nPrice:", computer.price, "\n\n")
        else:
            print("No inventory to display.")