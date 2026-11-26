from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Make sure it's a tuple (notice the comma at the end!)
    readonly_fields = ('admission_number',) 