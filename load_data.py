import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'students.settings')
django.setup()

from class1.models import Student

# The data
students_data = [
    ('John',   'Doe',      'ADM001', 'john.doe@school.edu',      '+254700000001', '2008-03-15', '2023-09-01', True, 'Allergic to peanuts'),
    ('Jane',   'Smith',    'ADM002', 'jane.smith@school.edu',    '+254700000002', '2009-07-22', '2023-09-01', True, 'Top performer in mathematics'),
    ('Michael','Brown',    'ADM003', 'michael.brown@school.edu', '+254700000003', '2008-11-05', '2023-09-01', True, 'Member of the debate club'),
    ('Sarah',  'Johnson',  'ADM004', 'sarah.johnson@school.edu', '+254700000004', '2009-01-30', '2023-09-01', True, ''),
    ('David',  'Williams', 'ADM005', 'david.w@school.edu',       '+254700000005', '2008-06-18', '2023-09-01', True, 'Needs extra time on exams'),
    ('Emily',  'Jones',    'ADM006', 'emily.jones@school.edu',   '+254700000006', '2009-04-12', '2023-09-01', True, 'School choir lead soprano'),
    ('Daniel', 'Garcia',   'ADM007', 'daniel.g@school.edu',      '+254700000007', '2008-09-25', '2023-09-01', True, ''),
    ('Olivia', 'Martinez', 'ADM008', 'olivia.m@school.edu',      '+254700000008', '2009-12-08', '2023-09-01', True, 'Member of the drama club'),
    ('James',  'Davis',    'ADM009', 'james.davis@school.edu',   '+254700000009', '2008-02-14', '2023-09-01', True, 'Captain of the football team'),
    ('Sophia', 'Rodriguez','ADM010', 'sophia.r@school.edu',      '+254700000010', '2009-08-19', '2023-09-01', True, ''),
    ('William','Wilson',   'ADM011', 'william.w@school.edu',     '+254700000011', '2008-05-03', '2023-09-01', True, 'Loves physics experiments'),
    ('Ava',    'Anderson', 'ADM012', 'ava.a@school.edu',         '+254700000012', '2009-10-27', '2023-09-01', True, 'Volunteers at the library'),
    ('Joseph', 'Thomas',   'ADM013', 'joseph.t@school.edu',      '+254700000013', '2008-07-11', '2023-09-01', True, ''),
    ('Mia',    'Taylor',   'ADM014', 'mia.taylor@school.edu',    '+254700000014', '2009-03-06', '2023-09-01', True, 'Art club president'),
    ('Charles','Moore',    'ADM015', 'charles.m@school.edu',     '+254700000015', '2008-12-22', '2023-09-01', True, 'Needs glasses during lectures'),
    ('Isabella','Jackson', 'ADM016', 'isabella.j@school.edu',    '+254700000016', '2009-06-15', '2023-09-01', True, ''),
    ('Thomas', 'White',    'ADM017', 'thomas.white@school.edu',  '+254700000017', '2008-08-30', '2023-09-01', True, 'Chess club champion'),
    ('Amelia', 'Harris',   'ADM018', 'amelia.h@school.edu',      '+254700000018', '2009-02-09', '2023-09-01', True, 'Science fair winner 2024'),
    ('Christopher','Martin','ADM019','chris.m@school.edu',       '+254700000019', '2008-04-17', '2023-09-01', True, ''),
    ('Harper', 'Thompson', 'ADM020', 'harper.t@school.edu',      '+254700000020', '2009-11-01', '2023-09-01', True, 'Transfer student from Nairobi'),
]

print("Starting to load data...")

# Loop through and create students
for s in students_data:
    # Check if student already exists to avoid duplicate errors
    if not Student.objects.filter(admission_number=s[2]).exists():
        Student.objects.create(
            first_name=s[0],
            last_name=s[1],
            admission_number=s[2],
            email=s[3],
            phone=s[4],
            date_of_birth=s[5],
            date_of_admission=s[6],
            is_active=s[7],
            special_notes=s[8]
        )

print("✅ Success! 20 students loaded into the database.")