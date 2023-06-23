"""form_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from form_app import views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('register',views.register,name="register"),
    path('logout',views.logout_user,name="logout"),

    path('home',views.dashboard,name="home"),
    path('bms_home',views.bms_home,name="bms-home"),
    path('bammc_home',views.bammc_home,name="bammc-home"),

    path('doLogin',views.doLogin),
    path('register_save',views.register_save,name="user_registration"),
    path('register_otp_check',views.register_check,name="register_check"),
    path('register_check_save',views.register_check_save,name="register_check_save"),



    path('fy_bms_form',views.fy_bms_form_view,name="fy_bms_form"),
    path('fy_bms_save',views.fy_bms_form_save,name="fy_bms_save"),

    path('fy_bammc_form',views.fy_bammc_form_view,name="fy_bammc_form"),
    path('fy_bammc_save',views.fy_bammc_form_save,name="fy_bammc_save"),

    path('sy_bms_market_form',views.sy_bms_market_form_view,name="sy_bms_market_form"),
    path('sy_bms_market_save',views.sy_bms_market_form_save,name="sy_bms_market_save"),

    path('sy_bms_hr_form',views.sy_bms_hr_form_view,name="sy_bms_hr_form"),
    path('sy_bms_hr_save',views.sy_bms_hr_form_save,name="sy_bms_hr_save"),

    path('sy_bammc_form',views.sy_bammc_form_view,name="sy_bammc_form"),
    path('sy_bammc_save',views.sy_bammc_form_save,name="sy_bammc_save"),

    path('sy_bms_market_form',views.sy_bms_market_form_view,name="sy_bms_market_form"),
    path('sy_bms_market_save',views.sy_bms_market_form_save,name="sy_bms_market_save"),

    path('ty_bammc_advert_form',views.ty_bammc_advert_form_view,name="ty_bammc_advert_form"),
    path('ty_bammc_advert_form_save',views.ty_bammc_advert_form_save,name="ty_bammc_advert_form_save"),

    path('ty_bammc_journal_form',views.ty_bammc_journal_form_view,name="ty_bammc_journal_form"),
    path('ty_bammc_journal_form_save',views.ty_bammc_journal_form_save,name="ty_bammc_journal_form_save"),

    path('ty_bms_hr_form',views.ty_bms_hr_form_view,name="ty_bms_hr_form"),
    path('ty_bms_hr_form_save',views.ty_bms_hr_form_save,name="ty_bms_hr_form_save"),

    path('ty_bms_market_form',views.ty_bms_market_form_view,name="ty_bms_market_form"),
    path('ty_bms_market_form_save',views.ty_bms_market_form_save,name="ty_bms_market_form_save"),

    path("view_accounts",views.manage_account,name="manage_accounts"),
    path('view_ssc_details',views.ssc_marksheet,name="ssc_marksheet"),
    path('view_hsc_details',views.hsc_marksheet,name="hsc_marksheet"),
    path('view_fy_sem1_details',views.fy_sem1_marksheet,name="fy_sem1_marksheet"),
    path('view_fy_sem2_details',views.fy_sem2_marksheet,name="fy_sem2_marksheet"),
    path('view_sy_sem1_details',views.sy_sem1_marksheet,name="sy_sem1_marksheet"),
    path('view_sy_sem2_details',views.sy_sem2_marksheet,name="sy_sem2_marksheet"),
    path('view_document',views.document_view,name="document_view"),
    path('document_save',views.document_save,name="document_save"),

    path('add_session',views.add_session,name="add_session"),
    path('add_session_save', views.add_session_save,name="add_session_save"),
    path('view_session',views.view_session,name="view_session"),
    path('delete_session/<str:session_id>',views.delete_session,name="delete_session"),
    path('view_submitted_forms',views.submitted_form,name="view_submitted_forms"),
    path('print_form/<str:form_id>',views.print_form_view,name="print"),

]