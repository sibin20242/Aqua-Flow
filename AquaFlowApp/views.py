from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import * 
from .forms import * 
from django.http import HttpResponse


# Create your views here.
# ////////////////////////////////////// ADMINISTRATION //////////////////////////////////////////////

class Authority(View):
    def get(self,request):
        obj = authority_model.objects.all()
        return render(request,"ADMINISTRATION/authority.html", {"obj":obj})


class AddAuthority(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/addauthority.html")
    def post(self, request):
        username = request.POST['username']
        password = request.POST['pass']
        repassword = request.POST['repass']
        if password == repassword:
            obj = Login_model.objects.create(Username=username,Password=password, Type='Authority')
            obj.save()
            return HttpResponse('''<script>alert("Authority Added Succesfully");window.location="/authority"</script>''')
        else:
            return HttpResponse('''<script>alert("Password Not Matched");window.location="/authority"</script>''')




class Addlist1(View):
     def get(self,request):
        obj = Login_model.objects.filter(Type='Authority')
        return render(request,"ADMINISTRATION/addlist1.html", {"obj":obj})

class RemoveAuthority(View):
    def get(self,request, auth_id):
        login_obj = Login_model.objects.get(id=auth_id)
        login_obj.delete()
        return HttpResponse('''<script>alert("delete succesfully");window.location="/authority"</script>''');

class Removeaddlist1(View):
    def get(self,request, auth_id):
        login_obj = Login_model.objects.get(id=auth_id)
        login_obj.delete()
        return HttpResponse('''<script>alert("delete succesfully");window.location="/addlist1"</script>''');


class Addlist(View):
     def get(self,request):
        obj = Login_model.objects.filter(Type='Staff')
        return render(request,"ADMINISTRATION/addlist.html", {"obj":obj})

class Staff(View):
    def get(self,request):
        obj = staff_model.objects.all()
        return render(request,"ADMINISTRATION/staff.html", {"obj":obj})

class AddStaff(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/addstaff.html")
    def post(self, request):
        username = request.POST['username']
        password = request.POST['pass']
        repassword = request.POST['repass']
        if password == repassword:
            obj = Login_model.objects.create(Username=username,Password=password, Type='Staff')
            obj.save()
            return HttpResponse('''<script>alert("Staff Added Succesfully");window.location="/addlist"</script>''')
        else:
            return HttpResponse('''<script>alert("Password Not Matched");window.location="/addlist"</script>''')

class RemoveStaff(View):
    def get(self,request, staff_id):
        login_obj = Login_model.objects.get(id=staff_id)
        login_obj.delete()
        return HttpResponse('''<script>alert("delete succesfully");window.location="/staff"</script>''')

class Removeaddlist(View):
    def get(self,request, staff_id):
        login_obj = Login_model.objects.get(id=staff_id)
        login_obj.delete()
        return HttpResponse('''<script>alert("delete succesfully");window.location="/addlist"</script>''')






class Area(View):
    def get(self,request):
        obj = area_model.objects.all()
        return render(request,"ADMINISTRATION/area.html", {"obj":obj})


class view_area(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/view_areas.html")



class Changep(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/changep.html")


class Complaint(View):
    def get(self,request):
        obj = complaints_model.objects.all()
        return render(request,"ADMINISTRATION/complaint.html", {"obj":obj})
        


class Feedback(View):
    def get(self,request):
        obj = feedback_model.objects.all()
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
        request.session['userid']=login_obj.id
        print(request.session['userid'])
        if login_obj.Type=="Admin":
            return HttpResponse('''<script>alert("login succesfully");window.location="/home"</script>''')
        elif login_obj.Type=="Authority":
            return HttpResponse('''<script>alert("login succesfully");window.location="/home1"</script>''')
        else:
         return HttpResponse('''<script>alert("login failed");window.location="/login"</script>''')

class Logout(View):
    def get(self,request):
        request.session.flush()
        return HttpResponse('''<script>alert("logout succesfully");window.location="/"</script>''')
        


class OTP(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/otp.html")



class Sign(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/sign.html")

class Time(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/time.html")

class User(View):
    def get(self,request):
        obj = user_model.objects.all()
        return render(request,"ADMINISTRATION/user.html", {"obj":obj})

class RemoveUser(View):
    def get(self,request, user_id):
        login_obj = Login_model.objects.get(id=user_id)
        login_obj.delete()
        return HttpResponse('''<script>alert("delete succesfully");window.location="/user"</script>''');

        
class WorkReport(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/workreport.html")

# ///////////////////////////////////// AUTH /////////////////////////////////////////////


class Area(View):
    def get(self,request):
        return render(request,"AUTHORITY/area.html")

class AssignedWork(View):
    def get(self,request):
        obj = assignedwork_model.objects.all()
        return render(request,"AUTHORITY/assignwork.html", {"obj":obj})        

class Changep(View):
    def get(self,request):
        return render(request,"AUTHORITY/changep.html")



class Feedback(View):
    def get(self,request):
        obj = feedback_model.objects.all()
        return render(request,"AUTHORITY/feedback.html", {"obj":obj})

class Complaint(View):
    def get(self,request):
        obj = complaints_model.objects.all()
        return render(request,"AUTHORITY/complaint.html", {"obj":obj})
        

class Forgetp(View):
    def get(self,request):
        return render(request,"AUTHORITY/forgetp.html")

class Home1(View):
    def get(self,request):
        return render(request,"AUTHORITY/home1.html")


class OTP(View):
    def get(self,request):
        return render(request,"AUTHORITY/otp.html")

class Profile(View):
    def get(self,request, id):
        c=Login_model.objects.filter(id=id).first()
        return render(request,"AUTHORITY/profile.html", {"c":c})

class EditProfile(View):
    def get(self,request, id):
        # c = get_object_or_404(Login_model, id=id)
        obj=authority_model.objects.get(LOGIN=id)
        print(obj)
        return render(request,"AUTHORITY/editprofile.html",{'val':obj})
    def post (self,request, id):        
        c = get_object_or_404(authority_model, LOGIN=id)
        ii=request.POST['First_name']
        form=ProfileForm(request.POST,instance=c)
        if form.is_valid():
            form.save()
            return render(request,"AUTHORITY/editprofile.html",{'val':c})


class Request(View):
    def get(self,request):
        return render(request,"AUTHORITY/request.html")

class RequestView(View):
    def get(self,request):
        return render(request,"AUTHORITY/requestview.html")          

class Sign(View):
    def get(self,request):
        return render(request,"AUTHORITY/sign.html")



class WorkReport(View):
    def get(self,request):
        obj = report_model.objects.all()
        return render(request,"AUTHORITY/workreport.html", {"obj":obj})