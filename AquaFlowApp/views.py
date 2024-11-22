from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import * 
from django.http import HttpResponse
# Create your views here.
# ////////////////////////////////////// ADMINISTRATION //////////////////////////////////////////////
class AddAuthority(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/addauthority.html")
        
class AddStaff(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/addstaff.html")
class Area(View):
    def get(self,request):
        obj = area_model.objects.all()
        return render(request,"ADMINISTRATION/area.html", {"obj":obj})
class view_area(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/view_areas.html")
class Authority(View):
    def get(self,request):
        obj = authority_model.objects.all()
        return render(request,"ADMINISTRATION/authority.html", {"obj":obj})
class Changep(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/changep.html")
class Complaint(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/complaint.html")
class EditProfile(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/editprofile.html")
class Feedback(View):
    def get(self,request):
        obj = feedback_model.objects.all()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<", obj )
        return render(request,"ADMINISTRATION/feedback.html", {"obj":obj})
class Forgetp(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/forgetp.html")
class Home(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/home.html")
class Login(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/login.html")
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=Login_model.objects.get(Username=username,Password=password)
        if login_obj.Type=="Admin":
            return HttpResponse('''<script>alert("login succesfully");window.location="/home"</script>''');
        elif login_obj.Type=="Authority":
            return HttpResponse('''<script>alert("login succesfully");window.location="/home1"</script>''');
        else:
         return HttpResponse('''<script>alert("login failed");window.location="/login"</script>''');
        
class OTP(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/otp.html")
class Profile(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/profile.html")
class Sign(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/sign.html")
class Staff(View):
    def get(self,request):
        obj = staff_model.objects.all()
        return render(request,"ADMINISTRATION/staff.html", {"obj":obj})
class Time(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/time.html")
class User(View):
    def get(self,request):
        obj = user_model.objects.all()
        return render(request,"ADMINISTRATION/user.html", {"obj":obj})
class WorkReport(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/workreport.html")

# ///////////////////////////////////// AUTH /////////////////////////////////////////////


# class Area(View):
#     def get(self,request):
#         return render(request,"ADMINISTRATION/area.html")
class AssignedWork(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/assignedwork.html")        
class Changep(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/changep.html")
class Complaint(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/complaint.html")
class EditProfile(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/editprofile.html")
# class Feedback(View):
#     def get(self,request):
#         return render(request,"ADMINISTRATION/feedback.html")
class Forgetp(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/forgetp.html")
class Home(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/home.html")
class OTP(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/otp.html")
class Profile(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/profile.html")
class Request(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/request.html")
class RequestView(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/requestview.html")          
class Sign(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/sign.html")
# class Staff(View):
#     def get(self,request):
#         return render(request,"ADMINISTRATION/staff.html")
# class User(View):
#     def get(self,request):
#         return render(request,"ADMINISTRATION/user.html")
class WorkReport(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/workreport.html")