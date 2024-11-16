from django.contrib import admin
from django.urls import path
from AquaFlowApp.views import *
urlpatterns = [

    # //////////////////////////////////////////// ADMIN /////////////////////////////////////////
    path('add_authority/',AddAuthority.as_view(), name="add_authority"),
    path('add_staff/',AddStaff.as_view(), name="add_staff"),
    path('area/',Area.as_view(), name="area"),
    path('authority/',Authority.as_view(), name="authority"),
    path('changep/',Changep.as_view(), name="changep"),
    path('complaint/',Complaint.as_view(), name="complaint"),
    path('edit_profile/',EditProfile.as_view(), name="edit_profile"),
    path('feedback/',Feedback.as_view(), name="feedback"),
    path('forgetp/',Forgetp.as_view(), name="forgetp"),
    path('home/',Home.as_view(), name="home"),
    path('login/',Login.as_view(), name="login"),
    path('otp/',OTP.as_view(), name="otp"),
    path('profile/',Profile.as_view(), name="profile"),
    path('sign/',Sign.as_view(), name="sign"),
    path('staff/',Staff.as_view(), name="staff"),
    path('time/',Time.as_view(), name="time"),
    path('user/',User.as_view(), name="user"),
    path('work_report/',WorkReport.as_view(), name="work_report"),
    

 # //////////////////////////////////////////// AUTHORITY /////////////////////////////////////////

    path('area/',Area.as_view(), name="area"),
    path('assigned_work/',AssignedWork.as_view(), name="assigned_work"),
    path('changep/',Changep.as_view(), name="changep"),
    path('complaint/',Complaint.as_view(), name="complaint"),
    path('edit_profile/',EditProfile.as_view(), name="edit_profile"),
    path('feedback/',Feedback.as_view(), name="feedback"),
    path('forgetp/',Forgetp.as_view(), name="forgetp"),
    path('home/',Home.as_view(), name="home"),
    path('login/',Login.as_view(), name="login"),
    path('otp/',OTP.as_view(), name="otp"),
    path('profile/',Profile.as_view(), name="profile"),
    path('request/',Request.as_view(), name="request"),
    path('request_view/',RequestView.as_view(), name="request_view"),
    path('sign/',Sign.as_view(), name="sign"),
    path('staff/',Staff.as_view(), name="staff"),
    path('user/',User.as_view(), name="user"),
    path('work_report/',WorkReport.as_view(), name="work_report"),
    
]
