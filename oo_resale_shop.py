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
        self.inventory.append(computer)
        

    def refurbish_computer(self, computer, new_os = None):
        computer.refurbish(computer.year_made, new_os)

    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Computer not found")
    
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory: 
            # For each item
            for computer in self.inventory:
                # Print its details
                print("Description:",computer.description,
                "\nProcessor Type:", computer.processor_type,
                "\nHard Drive Capacity:", computer.hard_drive_capacity,
                "\nMemory:", computer.memory,
                "\nOperating System:", computer.operating_system,
                "\nYear Made:", computer.year_made,
                "\nPrice:", computer.price, "\n\n")
        else:
            print("No inventory to display.")

def main():
    computer1 = Computer("Mac Pro", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "old os1", 2013, 1500)
    computer2 = Computer("desc", "processor", 1, 2, "old os2", 1999, 100)
    shop = ResaleShop()
    shop.buy(computer1)
    shop.buy(computer2)
    shop.refurbish_computer(computer1, "New OS")
    shop.refurbish_computer(computer2)
    shop.print_inventory()
    shop.sell(computer1)
    shop.print_inventory()
   
 

main()