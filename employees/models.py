from django.db import models
from organisation.models import Organisation

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.surename
    
class Availability(models.Model):
    
    AVALIABILITY_CHOICES = (
        ('Niedostepny', 'Niedostepny'),
        ('Dostepny', 'Dostepny'),
        ('Godziny', 'Dostepny w godzinach'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField()
    availability = models.CharField(max_length=20, choices=AVALIABILITY_CHOICES)
    availability_hours_start = models.TimeField(null=True, blank=True)
    availability_hours_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.employee.name + " " + self.employee.surename
