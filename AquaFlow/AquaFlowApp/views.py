from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import * 
from django.http import HttpResponse
# Create your views here.
# ////////////////////////////////////// ADMIN //////////////////////////////////////////////
class AddAuthority(View):
    def get(self,request):
        return render(request,"ADMIN/addauthority.html")
class AddStaff(View):
    def get(self,request):
        return render(request,"ADMIN/addstaff.html")
class Area(View):
    def get(self,request):
        return render(request,"ADMIN/area.html")
class Authority(View):
    def get(self,request):
        return render(request,"ADMIN/authority.html")
class Changep(View):
    def get(self,request):
        return render(request,"ADMIN/changep.html")
class Complaint(View):
    def get(self,request):
        return render(request,"ADMIN/complaint.html")
class EditProfile(View):
    def get(self,request):
        return render(request,"ADMIN/editprofile.html")
class Feedback(View):
    def get(self,request):
        return render(request,"ADMIN/feedback.html")
class Forgetp(View):
    def get(self,request):
        return render(request,"ADMIN/forgetp.html")
class Home(View):
    def get(self,request):
        return render(request,"ADMIN/home.html")
class Login(View):
    def get(self,request):
        return render(request,"ADMIN/login.html")
class OTP(View):
    def get(self,request):
        return render(request,"ADMIN/otp.html")
class Profile(View):
    def get(self,request):
        return render(request,"ADMIN/profile.html")
class Sign(View):
    def get(self,request):
        return render(request,"ADMIN/sign.html")
class Staff(View):
    def get(self,request):
        return render(request,"ADMIN/staff.html")
class Time(View):
    def get(self,request):
        return render(request,"ADMIN/time.html")
class User(View):
    def get(self,request):
        return render(request,"ADMIN/user.html")
class WorkReport(View):
    def get(self,request):
        return render(request,"ADMIN/workreport.html")

# ///////////////////////////////////// AUTH /////////////////////////////////////////////


class Area(View):
    def get(self,request):
        return render(request,"ADMIN/area.html")
class AssignedWork(View):
    def get(self,request):
        return render(request,"ADMIN/assignedwork.html")        
class Changep(View):
    def get(self,request):
        return render(request,"ADMIN/changep.html")
class Complaint(View):
    def get(self,request):
        return render(request,"ADMIN/complaint.html")
class EditProfile(View):
    def get(self,request):
        return render(request,"ADMIN/editprofile.html")
class Feedback(View):
    def get(self,request):
        return render(request,"ADMIN/feedback.html")
class Forgetp(View):
    def get(self,request):
        return render(request,"ADMIN/forgetp.html")
class Home(View):
    def get(self,request):
        return render(request,"ADMIN/home.html")
class Login(View):
    def get(self,request):
        return render(request,"ADMIN/login.html")
class OTP(View):
    def get(self,request):
        return render(request,"ADMIN/otp.html")
class Profile(View):
    def get(self,request):
        return render(request,"ADMIN/profile.html")
class Request(View):
    def get(self,request):
        return render(request,"ADMIN/request.html")
class RequestView(View):
    def get(self,request):
        return render(request,"ADMIN/requestview.html")          
class Sign(View):
    def get(self,request):
        return render(request,"ADMIN/sign.html")
class Staff(View):
    def get(self,request):
        return render(request,"ADMIN/staff.html")
class User(View):
    def get(self,request):
        return render(request,"ADMIN/user.html")
class WorkReport(View):
    def get(self,request):
        return render(request,"ADMIN/workreport.html")