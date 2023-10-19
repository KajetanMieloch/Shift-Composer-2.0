from django.db import models
from organisation.models import Organisation

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return  self.position
    

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return  self.organisation.name + " - " + self.name + " " + self.surname + " - " + self.position.position
    
class Availability(models.Model):
    
    AVALIABILITY_CHOICES = (
        ('available', 'Available'),
        ('available_in_hours', 'Available in hours'),
        ('unavailable', 'Unavailable'),
        ('holiday', 'Holiday'),
        ('sick', 'Sick'),
        ('unpaid', 'Unpaid'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField()
    availability = models.CharField(max_length=20, choices=AVALIABILITY_CHOICES)
    availability_hours_start = models.TimeField(null=True, blank=True)
    availability_hours_end = models.TimeField(null=True, blank=True)
    may_be_extended = models.BooleanField(default=False)

    def __str__(self):
        return  self.employee.name + " " + self.employee.surname + " - " + str(self.day) + " - " + self.availability

