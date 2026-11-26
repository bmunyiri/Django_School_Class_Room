from django.shortcuts import render
from class1.models import Student

# Create your views here.
def index(request):
    return render(request, 'students/index.html', context={'title': 'Class 1 Students', 'students': Student.objects.all().order_by('admission_number')})
