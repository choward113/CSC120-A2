class Computer:

    # What attributes will it need? 
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # What methods will you need?
    def refurbish(self, year_made: int, new_os = None) -> None:
        #Updates price based on year made and updates operating system if one is given 
        if self.year_made < 2000:
            self.price = 0 
        elif self.year_made < 2012:
            self.price = 250 
        elif self.year_made < 2018:
            self.price = 550 
        else:
            self.price = 1000 
        
        if new_os is not None:
            self.operating_system = new_os

    def update_price(self, new_price: int):
        #Updates price
        if new_price: 
            self.price = new_price
            print("The", self.description,"now costs", self.price)
        else:
            print("No new price was given")

    def update_operating_system(self, new_operating_system: str):
        #Updates operating system
        if new_operating_system:
            self.operating_system = new_operating_system
            print("The", self.description,"is now running", self.operating_system)
        else:
            print("No new operating system was given")

