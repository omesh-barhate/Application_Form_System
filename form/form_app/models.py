from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


class Account(AbstractUser):
    id=models.AutoField(primary_key=True)
    inhouse=models.BooleanField(default=False)
    middle_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    mobile_number=models.CharField(max_length=10,unique=True)
    dob = models.DateField()
    mother_first_name=models.CharField(max_length=255)
    father_first_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=UserManager()

class Personal_details(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    name_on_marksheet=models.CharField(max_length=255)
    name_in_hindi=models.CharField(max_length=100, db_collation='utf8_general_ci')
    mobile_number=models.CharField(max_length=10,unique=True)
    email = models.EmailField(max_length=254, unique=True)
    RESERVATION_CHOICES = (
        ('DT/VJ', 'DT/VJ'),
        ('NT', 'NT'),
        ('OBC', 'OBC'),
        ('OPEN', 'OPEN'),
        ('SBC', 'SBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
    )
    reservation = models.CharField(max_length=10, choices=RESERVATION_CHOICES)
    dob = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    ADMISSION_CHOICES = [
        ('Regular','Regular'),
        ('Provisional','Provisional'),
        ('Transfer','Transfer'),
    ]
    admission_type=models.CharField(max_length=11 ,choices=ADMISSION_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    aadhar_number = models.CharField(max_length=12, unique=True)
    address =models.CharField(max_length=255)
    account_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)


class Subjects_selected(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class ssc_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.IntegerField()
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()

class hsc_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.IntegerField()
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()

class fy_sem1_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.IntegerField()
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()

class fy_sem2_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.IntegerField()
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()

class sy_sem1_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.IntegerField()
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()

class sy_sem2_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.IntegerField()
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()


class Document(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    aadhar_card = models.BinaryField()
    candidate_sign = models.ImageField()
    parent_sign = models.ImageField()
    candidate_photo =models.ImageField()
    ssc_marksheet=models.BinaryField()
    hsc_marksheet=models.BinaryField()
    payment_receipt = models.BinaryField()
    leaving_certificate=models.BinaryField()
    mumbai_university_application =models.BinaryField()
    fy_sem1 =models.BinaryField(blank=False, null=False)
    fy_sem2 =models.BinaryField(blank=False, null=False)
    sy_sem1 =models.BinaryField(blank=False, null=False)
    sy_sem2 =models.BinaryField(blank=False, null=False)
    migration_certificate =models.BinaryField(blank=False, null=False)
    gap_certificate =models.BinaryField(blank=False, null=False)


class fy_bms_form(models.Model):
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
