from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from form_app.models import Account,Personal_details,Subject,Subjects_selected,SSC_marksheet,HSC_marksheet,Document,fy_bms_form,Course,FY_SEM1_marksheet,FY_SEM2_marksheet,SY_SEM1_marksheet,SY_SEM2_marksheet
from django.contrib.auth.decorators import login_required
from form_app.EmailBackend import EmailBackEnd

# Create your views here.
def test(request):
    return render(request,"test.html")

def main(request):
    return render(request,"login.html")

def register(request):
    id=request.user.id
    print(id)
    return render(request,"register.html")
    
@login_required
def dashboard(request):
    id=request.user.id
    print(id)
    return render(request,'dashboard.html')

def bms_home(request):
    return render(request,'bms-apply/bms-home.html')

def basic_form(request):
    my_object=Personal_details
    course_id=1
    semester=1
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=2
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)

    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2

    }
    return render(request,'bms-apply/fy_bms_form.html',context)

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponseRedirect("/home")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def register_check(request):

    return render(request,"register_check.html")

def register_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        middle_name=request.POST.get("middle_name")
        last_name=request.POST.get("last_name")
        inhouse = request.POST.get('category') == '1'
        mobile_number=request.POST.get("mobile_number")
        address=request.POST.get("address")
        email=request.POST.get("email")
        username=request.POST.get("username")
        mother_first_name=request.POST.get("mother_first_name")
        father_first_name=request.POST.get("father_first_name")
        date=request.POST.get("date")
        formatted_date =datetime.strptime(date, '%d/%m/%y')
        password=request.POST.get("password")
        try:
            user=Account.objects.create_user(first_name=first_name,middle_name=middle_name,last_name=last_name,inhouse=inhouse,mobile_number=mobile_number,address=address,email=email,username=username,mother_first_name=mother_first_name,father_first_name=father_first_name,dob=formatted_date,password=password)
            user.save()
            messages.success(request,"Account Created Successfully")
            return HttpResponseRedirect("/register_otp_check")
        except:
            messages.error(request,"Failed to create Account")
            return HttpResponseRedirect("/register_otp_check")

def fy_bms_form_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        marksheet_name = request.POST.get('marksheet_name')
        email = request.POST.get('email')
        devnagiri_name = request.POST.get('devnagiri_name')
        blood_group = request.POST.get('blood_group')
        date_of_birth = request.POST.get('date_of_birth')
        formatted_date_birth =datetime.strptime(date_of_birth, '%d/%m/%y')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=1)
        ##subjects
        sub_choosed = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
        date = datetime.strptime(passing_month, "%B %Y")
        month = date.strftime("%B")
        seat_number = request.POST.get('seat_number')
        marksheet_number = request.POST.get('marksheet_number')
        marks_obtained = request.POST.get('marks_obtained')
        marks_outof = request.POST.get('marks_outof')
        ## HSC
        board_name_hsc = request.POST.get('board_name_hsc')
        school_name_hsc = request.POST.get('school_name_hsc')
        medium_hsc = request.POST.get('medium_hsc')
        gpa_hsc = request.POST.get('gpa_hsc')
        passing_attempts_hsc = request.POST.get('passing_attempts_hsc')
        passing_month_hsc = request.POST.get('passing_month_hsc')
        date_hsc = datetime.strptime(passing_month_hsc, "%B %Y")
        month_hsc = date_hsc.strftime("%B")
        seat_number_hsc = request.POST.get('seat_number_hsc')
        marksheet_number_hsc = request.POST.get('marksheet_number_hsc')
        marks_obtained_hsc = request.POST.get('marks_obtained_hsc')
        marks_outof_hsc = request.POST.get('marks_outof_hsc')
        ## Documents
        aadhar_card = request.FILES.get('aaddhar_card')
        candidate_sign = request.FILES.get('candidate_signature')
        parent_sign = request.FILES.get('parent_signature')
        candidate_photo = request.FILES.get('candidate_photo')
        ssc_marksheet_pdf = request.FILES.get('ssc_marksheet')
        hsc_marksheet_pdf = request.FILES.get('hsc_marksheet')
        payment_receipt = request.FILES.get('payment_receipt')
        leaving_certificate = request.FILES.get('leaving_certificate')
        mumbai_university_application = request.FILES.get('mum_uni_application')
        fy_sem1 = request.FILES.get('fy_sem1')
        fy_sem2 = request.FILES.get('fy_sem2')
        sy_sem1 = request.FILES.get('sy_sem1')
        sy_sem2 = request.FILES.get('sy_sem2')
        migration_certificate = request.FILES.get('migration_certificate')
        gap_certificate = request.FILES.get('gap_certificate')
    
        person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance)
        person_detail.save()
        idp=person_detail.id
        print(idp)

        subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance)
        subjects_choosen.subjects.set(sub_choosed)

        subjects_choosen.save()
        ids=subjects_choosen.id
        print(ids)
        
        ssc=SSC_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,passing_year=month,cgpa=gpa,passing_attempts=passing_attempts,marks_obtained=marks_obtained,marks_out_of=marks_outof)
        ssc.save()
        idss=ssc.id
        print(idss)

        hsc=hsc_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,passing_year=month_hsc,cgpa=gpa_hsc,passing_attempts=passing_attempts_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc)
        hsc.save()
        idh=hsc.id
        print(idh)

        document= Document.objects.create(
                account_id=user,
                aadhar_card=aadhar_card.read() if aadhar_card else None,
                candidate_sign=candidate_sign.read() if candidate_sign else None,
                parent_sign=parent_sign.read() if parent_sign else None,
                candidate_photo=candidate_photo.read() if candidate_photo else None,
                ssc_marksheet=ssc_marksheet_pdf.read() if ssc_marksheet_pdf else None,
                hsc_marksheet=hsc_marksheet_pdf.read() if hsc_marksheet_pdf else None,
                payment_receipt=payment_receipt.read() if payment_receipt else None,
                leaving_certificate=leaving_certificate.read() if leaving_certificate else None,
                mumbai_university_application=mumbai_university_application.read() if mumbai_university_application else None,
                fy_sem1=fy_sem1.read() if fy_sem1 else None,
                fy_sem2=fy_sem2.read() if fy_sem2 else None,
                sy_sem1=sy_sem1.read() if sy_sem1 else None,
                sy_sem2=sy_sem2.read() if sy_sem2 else None,
                migration_certificate=migration_certificate.read() if migration_certificate else None,
                gap_certificate=gap_certificate.read() if gap_certificate else None
        )
        document.save()
        idd=document.id
        print(idd)
        document_instance=Document.objects.get(id=idd)
        person_detail_instance=Personal_details.objects.get(id=idp)
        ssc_instance=SSC_marksheet.objects.get(id=idss)
        hsc_instance=hsc_marksheet.objects.get(id=idh)
        sub_instance=Subjects_selected.objects.get(id=ids)
        form=fy_bms_form.objects.create(
            personal_detail=person_detail_instance,
            document=document_instance,
            ssc_id=ssc_instance,
            hsc_id=hsc_instance,
            subjects_choosen=sub_instance,

        )
        form.save()

        messages.success(request,"Form Created Successfully")
        return HttpResponseRedirect("/register_check")
    
        messages.error(request,"Failed to create Form")
        return HttpResponseRedirect("/register_check")

def manage_account(request):
    account=Account.objects.all()
    return render(request,"manage_account.html",{"accounts":account})

def ssc_marksheet(request):
    ssc=SSC_marksheet.objects.all()
    return render(request,"manage_ssc.html",{"ssc_details":ssc})

def hsc_marksheet(request):
    hsc=HSC_marksheet.objects.all()
    return render(request,"manage_hsc.html",{"hsc_details":hsc})

def fy_sem1_marksheet(request):
    sem1=FY_SEM1_marksheet.objects.all()
    return render(request,"manage_fy_sem1.html",{"sem1_details":sem1})

def fy_sem2_marksheet(request):
    sem2=FY_SEM2_marksheet.objects.all()
    return render(request,"manage_fy_sem2.html",{"sem2_details":sem2})

def sy_sem1_marksheet(request):
    sem3=SY_SEM1_marksheet.objects.all()
    return render(request,"sy_sem1.html",{"sem3_details":sem3})

def sy_sem2_marksheet(request):
    sem4=SY_SEM2_marksheet.objects.all()
    return render(request,"manage_sy_sem2.html",{"sem4_details":sem4})