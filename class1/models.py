from django.db import models
from datetime import date
from django.core.validators import RegexValidator

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True) # Added unique=True to match your DB screenshot
    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')]
    )
    date_of_birth = models.DateField()
    date_of_admission = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    special_notes = models.TextField(max_length=2000, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )