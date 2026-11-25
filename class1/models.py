from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    special_notes = models.TextField(max_length=2000)

class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students" 

def __str__():
    return(f"{{name}} is {{age}} years.This has been noted by the class teacher{{special_notes}}")

