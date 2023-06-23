from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest,HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from form_app.models import Account,Personal_details,Subject,Subjects_selected,SSC_marksheet,HSC_marksheet,Document,fy_bms_form,Course,FY_SEM1_marksheet,FY_SEM2_marksheet,SY_SEM1_marksheet,SY_SEM2_marksheet,AcademicYear,fy_bammc_form,sy_bms_market_form,sy_bms_hr_form,sy_bammc_form,ty_bammc_advert_form,ty_bammc_journal_form,ty_bms_hr_form,ty_bms_market_form
from django.contrib.auth.decorators import login_required
from form_app.EmailBackend import EmailBackEnd
from django.db.models import Q
# Create your views here.
def main(request):
    return render(request,"login.html")

def register(request):
    id=request.user.id
    print(id)
    return render(request,"register.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
    
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

def register_check_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        user_id=request.user.id
        otp=request.POST.get("otp_verification")
        print(otp)
        try:
            user = Account.objects.get(id=user_id)
            user.otp_verification = otp 
            user.save()
            messages.success(request,"OTP Verified Successfully")
            return HttpResponseRedirect("/home")
        except:    
            messages.error(request,"OTP Verification Failed")
            return HttpResponseRedirect("/register_otp_check")


def register_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        middle_name=request.POST.get("middle_name")
        last_name=request.POST.get("last_name")
        
        mobile_number=request.POST.get("mobile_number")
        address=request.POST.get("address")
        email=request.POST.get("email")
        username=request.POST.get("username")
        mother_first_name=request.POST.get("mother_first_name")
        father_first_name=request.POST.get("father_first_name")
        date=request.POST.get("date_of_birth")
        formatted_date =datetime.strptime(date, '%d/%m/%y')
        password=request.POST.get("password")
        try:
            user=Account.objects.create_user(first_name=first_name,middle_name=middle_name,last_name=last_name,mobile_number=mobile_number,address=address,email=email,username=username,mother_first_name=mother_first_name,father_first_name=father_first_name,dob=formatted_date,password=password)
            user.save()
            messages.success(request,"Account Created Successfully")
            return HttpResponseRedirect("/")
        except:
            messages.error(request,"Failed to create Account")
            return HttpResponseRedirect("/")



def dashboard(request):
    if request.user.is_authenticated and request.user.otp_verification == 1:
        id = request.user.id
        print(id)
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect("/register_otp_check") 

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

def bms_home(request):
    return render(request,'bms-apply/bms-home.html')

def bammc_home(request):
    return render(request,'bammc-apply/bammc-home.html')

def add_session(request):
    return render(request,'add_session.html')

def view_session(request):
    session=AcademicYear.objects.all()
    return render(request,'view_session.html',{"sessions":session})

def delete_session(request, session_id):
    sessiond = AcademicYear.objects.get(id=session_id)
    try:
        sessiond.delete()
        messages.success(request, "Session Deleted Successfully.")
        return HttpResponseRedirect('/view_session')
    except:
        messages.error(request, "Failed to Delete Session.")
        return HttpResponseRedirect('/view_session')

def add_session_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("add_session"))
    else:
        session_start_year=request.POST.get("session_start")
        session_end_year=request.POST.get("session_end")

        try:
            sessionyear=AcademicYear(session_start_year=session_start_year,session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Successfully Added Session")
            return HttpResponseRedirect(reverse("add_session"))
        except:
            messages.error(request, "Failed to Add Session")
            return HttpResponseRedirect(reverse("add_session"))

def fy_bms_form_view(request):
    my_object=Personal_details
    course_id=1
    semester=1
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=2
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bms-apply/fy_bms_form.html',context)

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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=1)
        ##subjects
        sub_choosed = [49,50,51,52,53,54,55,56,57,58,59,60,61,62]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=SSC_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,passing_year=passing_month,cgpa=gpa,passing_attempts=passing_attempts,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=HSC_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,passing_year=passing_month_hsc,cgpa=gpa_hsc,passing_attempts=passing_attempts_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=SSC_marksheet.objects.get(id=idss)
            hsc_instance=HSC_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=fy_bms_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                ssc_id=ssc_instance,
                hsc_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")

def fy_bammc_form_view(request):
    my_object=Personal_details
    course_id=6
    semester=1
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=2
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bammc-apply/fy_bammc_form.html',context)
    
def fy_bammc_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=6)
        ##subjects
        sub_choosed = [1,2,3,4,5,6,7,8,9,10,11,12]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=SSC_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,passing_year=passing_month,cgpa=gpa,passing_attempts=passing_attempts,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=HSC_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,passing_year=passing_month_hsc,cgpa=gpa_hsc,passing_attempts=passing_attempts_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=SSC_marksheet.objects.get(id=idss)
            hsc_instance=HSC_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=fy_bammc_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                ssc_id=ssc_instance,
                hsc_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")

 ##SY FORM Start

def sy_bms_market_form_view(request):
    my_object=Personal_details
    course_id=2
    semester=3
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=4
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bms-apply/sy_bms_market_form.html',context)
    
def sy_bms_market_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=2)
        ##subjects
        sub_choosed = [63,64,65,66,67,68,69,70,71,72,73,74,75,76]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=FY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=FY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=FY_SEM1_marksheet.objects.get(id=idss)
            hsc_instance=FY_SEM2_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=sy_bms_market_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                fy_sem1_id_id=ssc_instance,
                fy_sem2_id_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")

def sy_bms_hr_form_view(request):
    my_object=Personal_details
    course_id=3
    semester=3
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=4
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bms-apply/sy_bms_hr_form.html',context)
    
def sy_bms_hr_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=3)
        ##subjects
        sub_choosed = [77,78,79,80,81,82,83,84,85,86,87,88,89,90]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=FY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=FY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=FY_SEM1_marksheet.objects.get(id=idss)
            hsc_instance=FY_SEM2_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=sy_bms_hr_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                fy_sem1_id_id=ssc_instance,
                fy_sem2_id_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")

def sy_bammc_form_view(request):
    my_object=Personal_details
    course_id=7
    semester=3
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=4
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bammc-apply/sy_bammc_form.html',context)
    
def sy_bammc_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=7)
        ##subjects
        sub_choosed = [13,14,15,16,17,18,19,20,21,22,23,24]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=FY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=FY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=FY_SEM1_marksheet.objects.get(id=idss)
            hsc_instance=FY_SEM2_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=sy_bammc_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                fy_sem1_id_id=ssc_instance,
                fy_sem2_id_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")

## TY FORM START


def ty_bammc_advert_form_view(request):
    my_object=Personal_details
    course_id=9
    semester=5
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=6
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bammc-apply/ty_bammc_advert_form.html',context)
    
def ty_bammc_advert_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=9)
        ##subjects
        sub_choosed = [37,38,39,40,41,42,43,44,45,46,47,48]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=SY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=SY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=SY_SEM1_marksheet.objects.get(id=idss)
            hsc_instance=SY_SEM2_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=ty_bammc_advert_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                fy_sem1_id_id=ssc_instance,
                fy_sem2_id_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")


def ty_bammc_journal_form_view(request):
    my_object=Personal_details
    course_id=8
    semester=5
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=6
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bammc-apply/ty_bammc_journal_form.html',context)
    
def ty_bammc_journal_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=8)
        ##subjects
        sub_choosed = [25,26,27,28,29,30,31,32,33,34,35,36]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=SY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=SY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=SY_SEM1_marksheet.objects.get(id=idss)
            hsc_instance=SY_SEM2_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=ty_bammc_journal_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                fy_sem1_id_id=ssc_instance,
                fy_sem2_id_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")

### TY BMS START


def ty_bms_hr_form_view(request):
    my_object=Personal_details
    course_id=5
    semester=5
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=6
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bms-apply/ty_bms_hr_form.html',context)
    
def ty_bms_hr_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=5)
        ##subjects
        sub_choosed = [103,104,105,106,107,108,109,110,111,112,113,114]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
        try:
            session_instance=AcademicYear.objects.get(id=session)
            person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
            person_detail.save()
            idp=person_detail.id

            subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
            subjects_choosen.subjects.set(sub_choosed)

            subjects_choosen.save()
            ids=subjects_choosen.id
            
            ssc=SY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
            ssc.save()
            idss=ssc.id

            hsc=SY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
            hsc.save()
            idh=hsc.id

            document= Document.objects.create(
                    account_id=account_instance,
                    academic_id=session,
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
            document_instance=Document.objects.get(id=idd)
            person_detail_instance=Personal_details.objects.get(id=idp)
            ssc_instance=SY_SEM1_marksheet.objects.get(id=idss)
            hsc_instance=SY_SEM2_marksheet.objects.get(id=idh)
            sub_instance=Subjects_selected.objects.get(id=ids)
        
            form=ty_bms_hr_form.objects.create(
                personal_detail=person_detail_instance,
                document=document_instance,
                fy_sem1_id_id=ssc_instance,
                fy_sem2_id_id=hsc_instance,
                academic_id=session,
                subjects_choosen=sub_instance,
                account_id=account_instance,
            )
            form.save()

            messages.success(request,"Form Submitted Successfully")
            return HttpResponseRedirect("/home")
        except:
            messages.error(request,"Failed to Submit Form")
            return HttpResponseRedirect("/home")



def ty_bms_market_form_view(request):
    my_object=Personal_details
    course_id=4
    semester=5
    subjects = Subject.objects.filter(course_id=course_id, semester=semester)
    semester2=6
    subjects2 = Subject.objects.filter(course_id=course_id, semester=semester2)
    session_year_id=AcademicYear.objects.all()
    context = {
        'RESERVATION_CHOICES': my_object.RESERVATION_CHOICES,
        'GENDER_CHOICES': my_object.GENDER_CHOICES,
        'BLOOD_GROUP_CHOICES': my_object.BLOOD_GROUP_CHOICES,
        'ADMISSION_CHOICES': my_object.ADMISSION_CHOICES,
        'subjects': subjects,
        'subjects2':subjects2,
        "session_year_id":session_year_id
    }
    return render(request,'bms-apply/ty_bms_market_form.html',context)
    
def ty_bms_market_form_save(request):
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
        abc=request.POST.get('abc_id')
        phone_number = request.POST.get('phone_number')
        aadhar_number = request.POST.get('aadhar_number')
        reservation = request.POST.get('reservation')
        admission_type = request.POST.get('admission')
        session=request.POST.get('session_year_id')
        address = request.POST.get('address')
        user=request.user.id
        account_instance = Account.objects.get(id=user)
        course_instance=Course.objects.get(id=4)
        ##subjects
        sub_choosed = [91,92,93,94,95,96,97,98,99,100,101,102]
        print(sub_choosed)
        ## SSC
        board_name = request.POST.get('board_name')
        school_name = request.POST.get('school_name')
        medium = request.POST.get('medium')
        gpa = request.POST.get('gpa')
        passing_attempts = request.POST.get('passing_attempts')
        passing_month = request.POST.get('passing_month')
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
    
        session_instance=AcademicYear.objects.get(id=session)
        person_detail=Personal_details.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,name_on_marksheet=marksheet_name,name_in_hindi=devnagiri_name,email=email,mobile_number=phone_number,reservation=reservation,admission_type=admission_type,gender=gender,dob=formatted_date_birth,blood_group=blood_group,aadhar_number=aadhar_number,address=address,account_id=account_instance,academic_id=session,abc_id=abc)
        person_detail.save()
        idp=person_detail.id

        subjects_choosen=Subjects_selected.objects.create(course=course_instance,account=account_instance,academic_id=session)
        subjects_choosen.subjects.set(sub_choosed)

        subjects_choosen.save()
        ids=subjects_choosen.id
        
        ssc=SY_SEM1_marksheet.objects.create(university_name=board_name,school_name=school_name,medium=medium,seat_number=seat_number,marksheet_number=marksheet_number,cgpa=gpa,marks_obtained=marks_obtained,marks_out_of=marks_outof,account_id=user,academic_id=session)
        ssc.save()
        idss=ssc.id

        hsc=SY_SEM2_marksheet.objects.create(university_name=board_name_hsc,school_name=school_name_hsc,medium=medium_hsc,seat_number=seat_number_hsc,marksheet_number=marksheet_number_hsc,cgpa=gpa_hsc,marks_obtained=marks_obtained_hsc,marks_out_of=marks_outof_hsc,account_id=user,academic_id=session)
        hsc.save()
        idh=hsc.id

        document= Document.objects.create(
                account_id=account_instance,
                academic_id=session,
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
        document_instance=Document.objects.get(id=idd)
        person_detail_instance=Personal_details.objects.get(id=idp)
        ssc_instance=SY_SEM1_marksheet.objects.get(id=idss)
        hsc_instance=SY_SEM2_marksheet.objects.get(id=idh)
        sub_instance=Subjects_selected.objects.get(id=ids)
    
        form=ty_bms_market_form.objects.create(
            personal_detail=person_detail_instance,
            document=document_instance,
            fy_sem1_id_id=ssc_instance,
            fy_sem2_id_id=hsc_instance,
            academic_id=session,
            subjects_choosen=sub_instance,
            account_id=account_instance,
        )
        form.save()

        messages.success(request,"Form Submitted Successfully")
        return HttpResponseRedirect("/home")

        messages.error(request,"Failed to Submit Form")
        return HttpResponseRedirect("/home")


def submitted_form(request):
    form_models = [
        fy_bms_form,
        sy_bammc_form,
        sy_bms_hr_form,
        sy_bms_market_form,
        fy_bammc_form,
        ty_bammc_advert_form,
        ty_bammc_journal_form,
        ty_bms_hr_form,
        ty_bms_market_form,
        ]   
    filled_form= []
    account_id=request.user.id
     # Iterate over the form models and filter the objects based on user input and account ID
    for form_model in form_models:
        forms = form_model.objects.filter(account_id=account_id)
        filled_form.extend(forms)
    return render(request,"submitted_form.html",{'filled_forms': filled_form})
    
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML,CSS
import base64


def print_form_view(request,form_id,course_code):
    if course_code == "FYBMS":
        document = Document.objects.filter(fy_bms_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(fy_bms_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = fy_bms_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(fy_bms_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(fy_bms_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_fy_bms_form.html')
    elif course_code == "SYBMS_M":
        document = Document.objects.filter(sy_bms_market_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(sy_bms_market_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = sy_bms_market_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(sy_bms_market_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(sy_bms_market_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_sy_bms_form_m.html')
    elif course_code == "SYBMS_HR":
        document = Document.objects.filter(sy_bms_hr_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(sy_bms_hr_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = sy_bms_hr_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(sy_bms_hr_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(sy_bms_hr_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_sy_bms_form_hr.html')
    elif course_code == "TYBMS_M":
        document = Document.objects.filter(ty_bms_market_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(ty_bms_market_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = ty_bms_market_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(ty_bms_market_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(ty_bms_market_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_ty_bms_form_m.html')
    elif course_code == "TYBMS_HR":
        document = Document.objects.filter(ty_bms_hr_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(ty_bms_hr_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = ty_bms_hr_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(ty_bms_hr_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(ty_bms_hr_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_ty_bms_form_hr.html')
    elif course_code == "FYBAMMC":
        document = Document.objects.filter(fy_bammc_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(fy_bammc_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = fy_bammc_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(fy_bammc_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(fy_bammc_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_fy_bammc_form.html')
    elif course_code == "SYBAMMC":
        document = Document.objects.filter(sy_bammc_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(sy_bammc_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = sy_bammc_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(sy_bammc_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(sy_bammc_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_sy_bammc_form.html')
    elif course_code == "TYBAMMC_J":
        document = Document.objects.filter(ty_bammc_journal_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(ty_bammc_journal_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = ty_bammc_journal_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(ty_bammc_journal_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(ty_bammc_journal_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_ty_bammc_journal_form.html')
    else :
        document = Document.objects.filter(ty_bammc_advert_form__id=form_id).first()
        personal_details = Personal_details.objects.filter(ty_bammc_advert_form__id=form_id).first()
        
        first_name = personal_details.first_name
        middle_name = personal_details.middle_name
        last_name = personal_details.last_name
        name_on_marksheet = personal_details.name_on_marksheet
        name_in_hindi = personal_details.name_in_hindi
        mobile_number = personal_details.mobile_number
        email = personal_details.email
        reservation = personal_details.reservation
        dob = personal_details.dob
        gender = personal_details.gender
        blood_group = personal_details.blood_group
        admission_type = personal_details.admission_type
        aadhar_number = personal_details.aadhar_number
        address = personal_details.address
        abc_id = personal_details.abc_id
        academic = personal_details.academic.session_start_year
        academic_end = personal_details.academic.session_end_year

        submitted_document = []
        form = ty_bammc_advert_form.objects.filter(id=form_id).first()
        if form:
            document_fields = [
            ('aadhar_card', 'Aadhar Card'),
            ('candidate_sign', 'Candidate Signature'),
            ('parent_sign', 'Parent Signature'),
            ('candidate_photo', 'Candidate Photo'),
            ('ssc_marksheet', 'SSC Marksheet'),
            ('hsc_marksheet', 'HSC Marksheet'),
            ('payment_receipt', 'Payment Receipt'),
            ('leaving_certificate', 'Leaving Certificate'),
            ('mumbai_university_application', 'Mumbai University Application'),
            ('fy_sem1', 'FY Semester 1 Marksheet'),
            ('fy_sem2', 'FY Semester 2 Marksheet'),
            ('sy_sem1', 'SY Semester 1 Marksheet'),
            ('sy_sem2', 'SY Semester 2 Marksheet'),
            ('migration_certificate', 'Migration Certificate'),
            ('gap_certificate', 'Gap Certificate'),
        ]
        for field_name, field_label in document_fields:
            if getattr(form.document, field_name, None):
                submitted_document.append((field_label))

        candidate_photo = document.candidate_photo
        encoded_data = base64.b64encode(candidate_photo).decode('utf-8')
        course_code = form.subjects_choosen.course.course_code
        course_name = form.subjects_choosen.course.name
        account_id = form.account_id_id
        ssc=SSC_marksheet.objects.filter(ty_bammc_advert_form__id=form_id).first()
        ssc_obtained=ssc.marks_obtained
        ssc_out=ssc.marks_out_of
        ssc_gpa=ssc.cgpa

        hsc=HSC_marksheet.objects.filter(ty_bammc_advert_form__id=form_id).first()
        hsc_obtained=hsc.marks_obtained
        hsc_out=hsc.marks_out_of
        hsc_gpa=hsc.cgpa

        context = {
            'image_data': encoded_data,
            'course_code':course_code,
            'account_id': account_id,
            'course_name':course_name,
            'submitted_documents':submitted_document,
            'first_name':first_name,
            'form_id':form_id,
            'middle_name':middle_name,
            'last_name':last_name,
            'name_on_marksheet':name_on_marksheet,
            'mobile_number':mobile_number,
            'email':email,
            'reservation':reservation,
            'name_in_hindi':name_in_hindi,
            'dob':dob,
            'gender':gender,
            'blood_group':blood_group,
            'address':address,
            'admission_type':admission_type,
            'aadhar_number':aadhar_number,
            'abc_id':abc_id,
            'academic':academic,
            'academic_end':academic_end,
            'ssc_obtained':ssc_obtained,
            'ssc_out':ssc_out,
            'ssc_gpa':ssc_gpa,
            'hsc_obtained':hsc_obtained,
            'hsc_out':hsc_out,
            'hsc_gpa':hsc_gpa,
        }
        template = get_template('print/print_ty_bammc_advert_form.html')
    
    html = template.render(context)
    css = CSS(string='''
        @page {
            margin: 0.25in;
        }
        body {
            margin: 0;
            padding: 0;
        }
        .container {
            border: 4px solid black;
        }
        /* Add any additional styles as needed to remove borders or containers */
    ''')

    pdf_file = BytesIO()
    HTML(string=html).write_pdf(pdf_file, stylesheets=[css])

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=ST_Pauls_Application_Form.pdf'
    response.write(pdf_file.getvalue())

    return response

def document_view(request):
    document_fields = Document._meta.get_fields()
    field_names = ['aadhar_card',
        'candidate_sign',
        'parent_sign',
        'candidate_photo',
        'ssc_marksheet_pdf',
        'hsc_marksheet_pdf',
        'payment_receipt',
        'leaving_certificate',
        'mumbai_university_application',
        'fy_sem1' ,
        'fy_sem2' ,
        'sy_sem1' ,
        'sy_sem2',
        'migration_certificate' ,
        'gap_certificate',
    ]

    context = {'field_names': field_names}
    return render(request, 'document_form.html', context)

def document_save(request): 
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        row_id = request.POST.get('row_id')
        field_name = request.POST.get('field_name')

        if not row_id or not field_name:
            return HttpResponseBadRequest('Missing row ID or field name.')

        try:
            obj = Document.objects.get(id=row_id)
            blob_field = getattr(obj, field_name)
            
            file_extension = ''
            jpg_fields = ['candidate_sign', 'parent_sign', 'candidate_photo']  # Fields with ".jpg" extension
            pdf_fields = [field for field in Document._meta.fields if field.name not in jpg_fields]  # Fields with ".pdf" extension

            file_extension = 'jpg' if field_name in jpg_fields else 'pdf'
            response = HttpResponse(blob_field, content_type='application/octet-stream')
            
            # Set the Content-Disposition header with the file extension
            response['Content-Disposition'] = f'attachment; filename="{field_name}.{file_extension}"'
            return response
        except :
            messages.error(request,"Document not Found")
            return HttpResponseRedirect("/view_document")
