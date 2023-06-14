from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


class Account(AbstractUser):
    id=models.AutoField(primary_key=True)
    middle_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    mobile_number=models.CharField(max_length=10,unique=True)
    dob = models.DateField()
    mother_first_name=models.CharField(max_length=255)
    father_first_name=models.CharField(max_length=255)
    otp_verification=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=UserManager()

class AcademicYear(models.Model):
    id=models.AutoField(primary_key=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    object=models.Manager()

class Personal_details(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    name_on_marksheet=models.CharField(max_length=255)
    name_in_hindi=models.CharField(max_length=100, db_collation='utf8_general_ci')
    mobile_number=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
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
    aadhar_number = models.CharField(max_length=12)
    address =models.CharField(max_length=255)
    abc_id=models.CharField(max_length=16)
    account_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
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
    semester=models.CharField(max_length=1)


class Subjects_selected(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
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
    passing_year=models.CharField(max_length=255)
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class hsc_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    passing_year=models.CharField(max_length=255)
    passing_attempts=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class fy_sem1_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class fy_sem2_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class sy_sem1_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class sy_sem2_marksheet(models.Model):
    id=models.AutoField(primary_key=True)
    university_name=models.CharField(max_length=255)
    school_name= models.CharField(max_length=255)
    medium=models.CharField(max_length=10)
    seat_number=models.IntegerField()
    marksheet_number=models.IntegerField()
    marks_obtained=models.IntegerField()
    marks_out_of=models.IntegerField()
    cgpa=models.FloatField()
    account =models.ForeignKey(Account,on_delete=models.CASCADE)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Document(models.Model):
    id=models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    aadhar_card = models.BinaryField()
    candidate_sign = models.BinaryField()
    parent_sign = models.BinaryField()
    candidate_photo =models.BinaryField()
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
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class fy_bms_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class sy_bms_market_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class sy_bms_hr_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class ty_bms_market_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class ty_bms_hr_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class fy_bammc_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class sy_bammc_form(models.Model): 
    id=models.AutoField(primary_key=True)
    personal_detail=models.ForeignKey(Personal_details,on_delete=models.CASCADE)
    document =models.ForeignKey(Document,on_delete=models.CASCADE)
    ssc_id=models.ForeignKey(ssc_marksheet,on_delete=models.CASCADE)
    hsc_id=models.ForeignKey(hsc_marksheet,on_delete=models.CASCADE)
    subjects_choosen=models.ForeignKey(Subjects_selected,on_delete=models.CASCADE)
    otp_verification=models.BooleanField(default=False)
    academic=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    form_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()