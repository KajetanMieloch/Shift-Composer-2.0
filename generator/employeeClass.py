import datetime

class Employee:
    def __init__(self, id: int, name: str, surname: str, position: str, availability_mode: [[[datetime.date],[str]]], availability_hours: [[[datetime.date], [datetime.time],[datetime.time]]]):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.availability_mode = availability_mode
        self.availability_hours = availability_hours
    
    def getNames(self):
        return self.name + " " + self.surname
    
    def getPosition(self):
        return self.position
    
    def getAvailability(self):
        return self.availability_mode
    
    def getAvailabilityHours(self):
        return self.availability_hours
    
        
        