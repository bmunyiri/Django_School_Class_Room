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

    def save(self, *args, **kwargs):
        # Only generate a number if this is a NEW student (no number yet)
        if not self.admission_number:
            # Get the last student to find the highest number
            last_student = Student.objects.all().order_by('id').last()
            
            if not last_student:
                # If it's the very first student in the database
                self.admission_number = 'ADM001'
            else:
                # Extract the number part, add 1, and format it with leading zeros
                last_id = last_student.id
                new_id = last_id + 1
                self.admission_number = f'ADM{new_id:03d}' # 03d pads with zeros (e.g., ADM002)
                
        super().save(*args, **kwargs) # Call the real save method