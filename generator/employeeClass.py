import datetime

class Employee:
    def __init__(self, id: int, name: str, surname: str, position: str, availability_mode: [[[datetime.date],[str]]], availability_hours: [[[datetime.date], [datetime.time],[datetime.time]]]):
        self.id = id
        self.name = name
        self.surename = surname
        self.position = position
        self.availability_mode = availability_mode
        self.availability_hours = availability_hours
        
        