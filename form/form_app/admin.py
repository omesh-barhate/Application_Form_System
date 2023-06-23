from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from form_app.models import Account,Personal_details,Subject,Subjects_selected,SSC_marksheet,HSC_marksheet,Document,fy_bms_form,Course,FY_SEM1_marksheet,FY_SEM2_marksheet,SY_SEM1_marksheet,SY_SEM2_marksheet,AcademicYear,fy_bammc_form,sy_bms_market_form,sy_bms_hr_form,sy_bammc_form,ty_bammc_advert_form,ty_bammc_journal_form,ty_bms_hr_form,ty_bms_market_form

class UserModel(UserAdmin):
    pass
admin.site.register(Account,UserModel)

class PersonalModel(admin.ModelAdmin):
    list_display=["first_name","last_name"]
admin.site.register(Personal_details,PersonalModel)
class SubjectModel(ImportExportModelAdmin,admin.ModelAdmin):   
    list_display=["name","subject_code"]
admin.site.register(Subject,SubjectModel)
admin.site.register(Subjects_selected)
admin.site.register(SSC_marksheet)
admin.site.register(HSC_marksheet)
admin.site.register(FY_SEM1_marksheet)
admin.site.register(Document)
admin.site.register(FY_SEM2_marksheet)
admin.site.register(SY_SEM1_marksheet)
admin.site.register(SY_SEM2_marksheet)
class CourseModel(ImportExportModelAdmin,admin.ModelAdmin):   
    list_display=["name","course_code"]
admin.site.register(Course,CourseModel)
class AcademicModel(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=["id","session_start_year","session_end_year"]
admin.site.register(AcademicYear,AcademicModel)
admin.site.register(fy_bms_form)

admin.site.register(sy_bms_hr_form)

admin.site.register(sy_bms_market_form)

admin.site.register(ty_bms_hr_form)

admin.site.register(ty_bms_market_form)

admin.site.register(fy_bammc_form)

admin.site.register(sy_bammc_form)
admin.site.register(ty_bammc_advert_form)
admin.site.register(ty_bammc_journal_form)
