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



from django.contrib import messages

class Login(View):
    def get(self, request):
        return render(request, "ADMINISTRATION/login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Attempt to fetch the user from the database
            login_obj = Login_model.objects.get(Username=username, Password=password)
            request.session['userid'] = login_obj.id
            print(request.session['userid'])

            # Redirect based on the user's type
            if login_obj.Type == "Admin":
                # messages.success(request, "Login successful")
                return redirect('/home')
            elif login_obj.Type == "Authority":
                messages.success(request, "Login successful")
                return redirect('/home1')
            else:
                messages.error(request, "Login failed")
                return redirect('login')  # Assuming 'login' is the name of the login page URL pattern
        except Login_model.DoesNotExist:
            # Handle the case where the user does not exist
            messages.error(request, "Invalid username or password")
            return redirect('login')
            

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
        c=staff_model.objects.all()
        obj = assignedwork_model.objects.all()
        return render(request,"AUTHORITY/assignwork.html", {"obj":obj,"c":c})
        # return render(request,"AUTHORITY/assignwork.html", {"obj":obj})        

class Request(View):
    def get(self,request):
        obj = application_model.objects.all()
        return render(request,"AUTHORITY/request.html" , {"obj":obj})

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
        c=authority_model.objects.filter(LOGIN_id=id).first()
        print(c.Last_name)
        return render(request,"AUTHORITY/profile.html", {"val":c})

class EditProfile(View):
    def get(self,request, id):
        # c = get_object_or_404(Login_model, id=id)
        obj=authority_model.objects.get(LOGIN=id)
        return render(request,"AUTHORITY/editprofile.html",{'val':obj})
    def post (self,request, id):        
        obj=authority_model.objects.get(LOGIN=id)
        ii=request.POST['First_name']
        jj=request.POST['Last_name']
        kk=request.POST['Mid_name']
        print("first_name",ii)
        print("mid_name",kk)
        print("last_name",jj)
        form=ProfileForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return render(request,"AUTHORITY/editprofile.html",{'val':obj})




class RequestView(View):
    def get(self,request):
        return render(request,"AUTHORITY/requestview.html")          

class Sign(View):
    def get(self,request):
        return render(request,"AUTHORITY/sign.html")



class WorkReport(View):
    def get(self,request):
        obj = report_model.objects.all()
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%", obj)
        return render(request,"AUTHORITY/workreport.html", {"obj":obj})

class Authoritybase(View):
    def get(self,request):
        return render(request,"AUTHORITY/authoritybase.html")
        
# /////////////////////////////////////////USER API/////////////////////////////////////////////////


class UserReg(APIView):
    def post(self, request):
        user_serial = UserSerializer (data=request.data)
        login_serial = LoginSerializer (data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()
        if data_valid and login_valid:
            password = request.data['password' ]
            login_profile=login_serial.save(user_type="USER", password=password)
            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                        'user _error': user_serial.errors if not data_valid else None})
                    

class ViewStatus(APIView):
    def get(self, request):
        status = StatusTable.objects.all()
        Status_serializer=StatusSerializer(Status, many = True)
        return Response(Status_serializer.data)

class ViewTime(APIView):
    def get(self, request):
        Time = TimeTable.objects.all()
        Time_serializer=TimeSerializer(Time, many = True)
        return Response(Time_serializer.data)

class ViewBill(APIView):
    def get(self, request):
        Bill = StatusTable.objects.all()
        Bill_serializer=BillSerializer(Bill, many = True)
        return Response(Bill_serializer.data)

class ViewProfile(APIView):
    def get(self, request):
        Profile = ProfileTable.objects.all()
        Profile_serializer=ProfileSerializer(Profile, many = True)
        return Response(Profile_serializer.data)

class ViewComplaint(APIView):
    def get(self, request):
        Complaint = ComplaintTable.objects.all()
        Complaint_serializer=ComplaintSerializer(Complaint, many = True)
        return Response(Complaint_serializer.data)


# /////////////////////////////////////////STAFF API/////////////////////////////////////////////////





class ViewAssignedwork(APIView):
    def get(self, request):
        Assignedwork = AssignedworkTable.objects.all()
        Assignedwork_serializer=AssignedworkSerializer(Assignedwork, many = True)
        return Response(Assignedwork_serializer.data)

class ViewUserdetails(APIView):
    def get(self, request):
        Userdetails = UserdetailsTable.objects.all()
        Userdetails_serializer=UserdetailsSerializer(Userdetails, many = True)
        return Response(Userdetails_serializer.data)




