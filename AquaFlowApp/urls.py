from django.contrib import admin
from django.urls import path
from AquaFlowApp.views import *
urlpatterns = [

    # //////////////////////////////////////////// ADMIN /////////////////////////////////////////


    path('',Login.as_view(), name="login"),
    path('addauthority/',AddAuthority.as_view(), name="addauthority"),
    path('addlist1/',Addlist1.as_view(), name="addlist1"),
    path('remove_addlist1/<int:auth_id>',Removeaddlist1.as_view(), name="remove_addlist1"),
    path('remove_authority/<int:auth_id>',RemoveAuthority.as_view(), name="remove_authority"),
    path('addstaff/',AddStaff.as_view(), name="add_staff"),
    path('addlist/',Addlist.as_view(), name="addlist"),
    path('remove_addlist/<int:staff_id>',Removeaddlist.as_view(), name="remove_addlist"),
    path('remove_staff/<int:staff_id>',RemoveStaff.as_view(), name="remove_staff"),
    path('area/',Area.as_view(), name="area"),
    path('view_area/',view_area.as_view(), name="view_area"),
    path('authority/',Authority.as_view(), name="authority"),
    path('changep/',Changep.as_view(), name="changep"),
    path('complaint/',Complaint.as_view(), name="complaint"),
    path('feedback/',Feedback.as_view(), name="feedback"),
    path('forgetp/',Forgetp.as_view(), name="forgetp"),
    path('home/',Home.as_view(), name="home"),
    path('otp/',OTP.as_view(), name="otp"),
    path('sign/',Sign.as_view(), name="sign"),
    path('staff/',Staff.as_view(), name="staff"),
    path('time/',Time.as_view(), name="time"),
    path('user/',User.as_view(), name="user"),
    path('remove_user/<int:user_id>',RemoveUser.as_view(), name="remove_user"),
    path('work_report/',WorkReport.as_view(), name="work_report"),



    # //////////////////////////////////////////// AUTHORITY /////////////////////////////////////////


    path('area/',Area.as_view(), name="area"),
    path('assignedwork/',AssignedWork.as_view(), name="assignedwork"),
    path('changep/',Changep.as_view(), name="changep"),
    path('complaint/',Complaint.as_view(), name="complaint"),
    path('editprofile/<int:id>/',EditProfile.as_view(), name="editprofile"),
    path('feedback/',Feedback.as_view(), name="feedback"),
    path('forgetp/',Forgetp.as_view(), name="forgetp"),
    path('home1/',Home1.as_view(), name="home1"),
    path('otp/',OTP.as_view(), name="otp"),
    path('profile/<int:id>',Profile.as_view(), name="profile"),
    path('request/',Request.as_view(), name="request"),
    path('requestview/',RequestView.as_view(), name="requestview"),
    path('sign/',Sign.as_view(), name="sign"),
    path('workreport/',WorkReport.as_view(), name="workreport"),
    path('logout/',Logout.as_view(), name="logout"),
    path('authoritybase/',Authoritybase.as_view(), name="authoritybase"),






    #/////////////////////API///////////////////////////




    #////////////////////API USER//////////////////////

    path('userregapi/',UserReg.as_view() ,name="userreg"),
    path('Loginapi',Loginapi.as_view() , name="Login"),
    path('Statusapi/',ViewStatus.as_view() , name="ViewStatus"),
    path('Timeapi/',ViewTime.as_view() , name="ViewTime"),
    path('Billapi/',ViewBill.as_view() , name="ViewBill"),
    path('Profileapi/',ViewProfile.as_view() , name="ViewProfile"),
    path('Complaintapi/',ViewComplaint.as_view() , name="ViewComplaint"),
    path('AppliRegapi/',AppliReg.as_view() , name="AppliReg"),
    path('ComplaintRegapi/',ComplaintReg.as_view() , name="ComplaintReg"),
    path('ProfileRegapi/',ProfileReg.as_view() , name="ProfileReg"),
    path('Feedbackapi/',Feedback.as_view() , name="Feedback"),


    #////////////////////API STAFF//////////////////////

    path('Assignedworkapi/',ViewAssignedwork.as_view() , name="ViewAssignedwork"),
    path('Userdetailsapi/',ViewUserdetails.as_view() , name="ViewUserdetails"),
    path('UpdateReportapi/',UpdateReport.as_view() , name="UpdateReport"),
    path('MeterReadingapi/',MeterReading.as_view() , name="MeterReading"),

]
