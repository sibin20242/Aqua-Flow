from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import * 
from .forms import * 
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib import messages
from AquaFlowApp.serial import *





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
            return HttpResponse('''<script>alert("Authority Added Succesfully");window.location="/addlist1"</script>''')
        else:
            return HttpResponse('''<script>alert("Password Not Matched");window.location="/addauthority"</script>''')




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






# class Area(View):
#     def get(self,request):
#         obj = area_model.objects.all()
#         return render(request,"ADMINISTRATION/area.html", {"obj":obj})


# class view_area(View):
#     def get(self,request):
#         return render(request,"ADMINISTRATION/view_areas.html")





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



class adminarea(View):
    def get(self,request):
        obj = area_model.objects.all()
        return render(request,"ADMINISTRATION/area.html", {"areas":obj})
class AreaDetailView(View):
    def get(self, request, area_id):
        obj = area_model.objects.all()
        area = get_object_or_404(area_model, id=area_id)
        staffs = staff_model.objects.filter(AREA=area)
        users = user_model.objects.filter(Area=area)
        authorities = authority_model.objects.filter(AREA=area)
        
        return render(
            request, 
            "ADMINISTRATION/area_detail.html", 
            {"area": area, "staffs": staffs, "users": users, "authorities": authorities,"areas":obj}
        )

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
                # messages.success(request, "Login successful")
                return HttpResponse('''<script>alert("welcome Authority");window.location="/home1"</script>''')
       

               
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
from datetime import datetime
from django.http import JsonResponse
class Time(View):
    def get(self,request):
        return render(request,"ADMINISTRATION/time.html")

    def post(self, request, *args, **kwargs):
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')

        if not date_str or not time_str:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        try:
            date_obj = datetime.strptime(date_str, "%d %B %Y").date()
            time_obj = datetime.strptime(time_str, "%H:%M").time()

            # Save to the database
            time_entry, created = time_model.objects.get_or_create(Date=date_obj, defaults={'morning_Time': time_obj})

            if not created:
                time_entry.morning_Time = time_obj
                time_entry.save()

            return JsonResponse({'message': 'Time saved successfully!'})

        except ValueError:
            return JsonResponse({'error': 'Invalid date/time format'}, status=400)

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


# class Area(View):
#     def get(self,request):
#         return render(request,"AUTHORITY/area.html")

class AssignedWork(View):
    def get(self,request):
        complaints=complaints_model.objects.all()
        c=staff_model.objects.all()
        obj = assignedwork_model.objects.all()
        return render(request,"AUTHORITY/assignwork.html", {"obj":obj,"c":c,"complaints":complaints})
        # return render(request,"AUTHORITY/assignwork.html", {"obj":obj}) 

class approvedapplicationstatus(View):
    def get(self,request,id):
        apl=application_model.objects.filter(id=id).first()
        apl.Status="approved"
        apl.save()
        return HttpResponse('''<script>alert("application approved succesfully");window.location="/request"</script>''')


class AssignWorktostaff(View):
    def get(self,request,id):
        o=complaints_model.objects.filter(id=id)
        c=staff_model.objects.all()
        return render(request,'AUTHORITY/assignworktostaff.html',{"o":o,"c":c})

    def post(self,request,id):
        o=complaints_model.objects.filter(id=id).first()
        s=staff_model.objects.get(id=request.POST['staffid'])
        o.assignedstaff=s
        o.save()
        c=staff_model.objects.all()
        return redirect('assignedwork')  

class rejectapplicationstatus(View):
    def get(self,request,id):
        apl=application_model.objects.filter(id=id).first()
        apl.Status="reject"
        apl.save()
        return HttpResponse('''<script>alert("application rejected succesfully");window.location="/request"</script>''')

class penddingapplicationstatus(View):
    def get(self,request,id):
        apl=application_model.objects.filter(id=id).first()
        apl.Status="pendding"
        apl.save()
        return HttpResponse('''<script>alert("application pendding succesfully");window.location="/request"</script>''')





class Request(View):
    def get(self,request):
        obj = application_model.objects.all()
        return render(request,"AUTHORITY/request.html" , {"obj":obj})

class Changep(View):
    def get(self,request):
        return render(request,"AUTHORITY/Changep.html")

    def post(self,request):
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        print(new_password,confirm_password)

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request,'AUTHORITY/verify_otp.html')

        try:
            user = Login_model.objects.filter(Username=email).first()

            if user.Otp == otp:
                user.Password = new_password  # Store password directly (Hashing should be done for security)
                user.Otp = None  # Clear OTP after reset
                user.save()
                messages.success(request, "Password changed successfully. You can now log in.")
                return redirect('login')

            else:
                messages.error(request, "Invalid OTP.")
                return render(request, 'verify_otp.html')

        except Login_model.DoesNotExist:
            messages.error(request, "Invalid email or OTP.")
            return render(request, 'verify_otp.html')
        

class ChangePassword(View):
    def get(self, request):
        return render(request, "AUTHORITY/ChangeP.html")
    def post(self, request):
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Fetch the user from the Login_Model
        user = Login_model.objects.get(id=request.session.get('userid'))
        print('=======================================================>', user.Password)
        print('========================================================>',current_password)

        # Check if the current password matches
        if user.Password!=current_password:
            return HttpResponse('''<script>alert('incorrect current pass');window.location='/changepass'</script>''') 
        
        # Validate if new passwords match
        if new_password != confirm_password:
            return HttpResponse('''<script>alert('New password and confirm password do not match.');window.location='/changepass'</script>''') 
        
        # Hash and update the new password
        user.Password = new_password
        user.save()
        return HttpResponse('''<script>alert('Your password has been successfully changed..');window.location='/changepass'</script>''') 
        



class Feedbacks(View):
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
        c=Login_model.objects.get(id=id)
        print('----------------->', c.id)
        try:
            obj=authority_model.objects.get(LOGIN_id=c.id)
            return render(request,"AUTHORITY/profile.html", {"val":obj})
        except:
            return render(request,"AUTHORITY/profile.html")

class EditProfile(View):
    def get(self,request, id):
        try:
            c = get_object_or_404(Login_model, id=id)
            print('--------------->', id)
            obj=Login_model.objects.get(id=id)
            obj1=authority_model.objects.get(LOGIN=id)
            return render(request,"AUTHORITY/editprofile.html",{'val':obj1})
        except:
            c = get_object_or_404(Login_model, id=id)
            print('--------------->', id)
            obj=Login_model.objects.get(id=id)

            return render(request,"AUTHORITY/editprofile.html",{'val':obj})

    def post (self,request, id): 
        c=Login_model.objects.get(id=id)

        try:
            obj=authority_model.objects.get(LOGIN=id)
            ii=request.POST['First_name']
            jj=request.POST['Last_name']
            kk=request.POST['Mid_name']
            form=ProfileForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return render(request,"AUTHORITY/editprofile.html",{'val':obj})
        except:
            form=ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                f=form.save(commit=False)
                f.LOGIN=c
                f.save()
                return redirect('home1')







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
class Userreg1(APIView):
    def post(self,request):
        d=LoginSerializer(data=request.data)
        e=signupSerializer(data=request.data)
        u=d.is_valid()
        s=e.is_valid()
        if u and s:
            g=d.save(Type='User')
            e.save(LOGIN=g)
            return Response(e.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': d.errors if not login_valid else None,
                        'user _error': e.errors if not data_valid else None})

class UserReg(APIView):
    def post(self, request):
        email=request.data.get("email")
        username=request.data.get("username")
        password=request.data.get("password")
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
                    
class Loginapi(APIView):
    def post(self, request):
        print("&&&&&&&&&&&&&")
        response_dict={}
        username=request.data.get("email")
        password=request.data.get("password")
        print("&&&&&&&&&&&&&", username, password)  
        try:
           user = Login_model.objects.get(Username=username,Password=password)
        except Login_model.DoesNotExist:
            response_dict["message"] = "No account is found for this username.Please Signup."
            return Response(response_dict)
        if user.Type == "User":
            response_dict ={
                "login_id": user.id,
                "user_type": user.Type,
                "status": "success",
            }
            print("^^^^^^^^^^^^^^^^", response_dict)

            return Response(response_dict, status=status.HTTP_200_OK)
        elif user.Type == "Staff":
            response_dict = {
                "login_id": user.id,
                "user_type": user.Type,
                "status": "success",
            }
            print("^^^^^^^^^^^^^^^^", response_dict)
            return Response(response_dict, status=status.HTTP_200_OK)
       

class ViewStatus(APIView):
    def get(self, request):
        status = StatusTable.objects.all()
        Status_serializer=StatusSerializer(Status, many = True)
        return Response(Status_serializer.data)

class ViewTime(APIView):
    def get(self, request,dat):
        Time = time_model.objects.filter(Date=dat).all()
        Time_serializer=TimeSerializer(Time, many = True)
        return Response(Time_serializer.data)


class ViewBill(APIView):
    def get(self, request):
        Bill = bill_model.objects.all()
        Bill_serializer=BillSerializer(Bill, many = True)
        return Response(Bill_serializer.data)

class ViewProfile(APIView):
    def get(self, request,id):
        Profile = user_model.objects.get(LOGIN__id=id)
        Profile_serializer=ProfileSerializer(Profile)
        return Response(Profile_serializer.data)

class ViewComplaint(APIView):
    def get(self, request):
        Complaint = complaints_model.objects.all()
        Complaint_serializer=ComplaintSerializer(Complaint, many = True)
        return Response(Complaint_serializer.data)

        
class AppliReg(APIView):
    def post(self, request, id):
        Application_Serializer = ApplicationSerializer(data=request.data)
        print("@@@@@@@@@@@@@@@@@@@@@@@", request.data)
        if Application_Serializer.is_valid():
            user_obj=user_model.objects.get(LOGIN_id=id)
            Application_Serializer.save(USER=user_obj)
            return Response(Application_Serializer.data, status=status.HTTP_201_CREATED)
        return Response({'application_error': Application_Serializer.errors if not login_valid else None})


class ComplaintReg(APIView):
    def post(self, request):
        Complaint_Serializer = ComplaintSerializer (data=request.data)
        if Complaint_Serializer.is_valid():
            Complaint_Serializer.save()
            return Response(Complaint_Serializer.data, status=status.HTTP_201_CREATED)
        return Response({'complaint_error': Complaint_Serializer.errors if not login_valid else None})

class ProfileReg(APIView):
    def put(self, request,id):
        Profile = user_model.objects.get(LOGIN__id=id)
        Profile_Serializer = ProfileSerializer (Profile,data=request.data)
        if Profile_Serializer.is_valid():
            Profile_Serializer.save()
            return Response(Profile_Serializer.data, status=status.HTTP_201_CREATED)
        return Response({'profile_error': Profile_Serializer.errors if not login_valid else None})


class Feedback(APIView):
    def post(self, request):
        data=request.data
        v=user_model.objects.filter(LOGIN__id=request.data['USER']).first()
        data['USER']=v.pk
        Feedback_Serializer = FeedbackSerializer (data=data)
        if Feedback_Serializer.is_valid():
            Feedback_Serializer.save()
            return Response(Feedback_Serializer.data, status=status.HTTP_201_CREATED)
        return Response({'feedback_error': Feedback_Serializer.errors if not login_valid else None})


class AUTHORITYChat (View):
     def get(self, request):
        user_id=request.session.get('userid')
        print(user_id)
        return render (request, 'AUTHORITY/chat.html',{'user_id':user_id})

class ChatAPIView(APIView):

    def get(self, request,sender_id,receiver_id):
        user = request.user
        
        if not receiver_id:
            return Response({"error": "receiver_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            receiver = LoginTable.objects.get(id=receiver_id)
        except LoginTable.DoesNotExist:
            return Response({"error": "Receiver does not exist"}, status=status.HTTP_404_NOT_FOUND)

        chats = Chat.objects.filter(
            (models.Q(sender=sender_id) & models.Q(receiver=receiver_id)) |
            (models.Q(sender=receiver_id) & models.Q(receiver=sender_id))
        ).order_by('timestamp')
        print("mmmmm",chats)

        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request,sender_id,receiver_id):
        """
        Send a chat message from the logged-in user to a specific receiver.
        """
        user = sender_id
        receiver_id=receiver_id
        data = request.data
        data['sender'] = user 
        data['receiver']= receiver_id# Set the sender to the logged-in user

        serializer = ChatSerializer1(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChattedUsersAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request,userid):
        """
        Get a list of users the logged-in user has chatted with.
        """
        user = userid  # Logged-in user
        print(user)
        
        # Fetch all users the logged-in user has sent or received messages with
        sent_chats = Chat.objects.filter(sender=user).values_list('receiver', flat=True)
        received_chats = Chat.objects.filter(receiver=user).values_list('sender', flat=True)
        
        # Combine and get unique user IDs
        chatted_user_ids = set(sent_chats) | set(received_chats)
        
        # Fetch user details for these IDs
        chatted_users = LoginTable.objects.filter(id__in=chatted_user_ids)
        
        # Serialize the user details
        serializer = ChattedUsersSerializer1(chatted_users, many=True)
        print(serializer.data)
        
        return Response(serializer.data)        


# /////////////////////////////////////////STAFF API/////////////////////////////////////////////////





class ViewAssignedwork(APIView):
    def get(self, request, id):
        Assignedwork = assignedwork_model.objects.filter(STAFF__LOGIN__id=id)

        if not Assignedwork.exists():
            return Response({"message": "No assigned work found"}, status=404)

        Assignedwork_serializer = AssignedworkSerializer(Assignedwork, many=True)
        return Response(Assignedwork_serializer.data)


class ViewUserdetails(APIView):
    def get(self, request):
        Userdetails = user_model.objects.all()
        Userdetails_serializer=UserdetailsSerializer(Userdetails, many = True)
        return Response(Userdetails_serializer.data)

class UpdateReport(APIView):
    def post(self, request):
        Report_Serializer = UpdateReportSerializer(data=request.data)
        staff_id = request.data.get('STAFF')
        staff_obj = staff_model.objects.get(LOGIN_id=staff_id)
        print(request.data)
        if Report_Serializer.is_valid():
            print('------valid->')
            Report_Serializer.save(STAFF=staff_obj)
            return Response(Report_Serializer.data, status=status.HTTP_200_OK)

        # Always return a response, even if `login_valid` is False
        return Response({'report_error': Report_Serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class MeterReading(APIView):
    def post(self, request):
        Meter_Serializer = MeterReadingSerializer (data=request.data)
        if Meter_Serializer.is_valid():
            Meter_Serializer.save(LOGIN=login_profile)
            return Response(Meter_Serializer.data, status=status.HTTP_201_CREATED)
        return Response({'meter_error': Meter_Serializer.errors if not login_valid else None})

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class ChatAPIView(APIView):

    def get(self, request,sender_id,receiver_id):
        user = request.user
        
        if not receiver_id:
            return Response({"error": "receiver_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            receiver = Login_model.objects.get(id=receiver_id)
        except Login_model.DoesNotExist:
            return Response({"error": "Receiver does not exist"}, status=status.HTTP_404_NOT_FOUND)

        chats = Chat.objects.filter(
            (models.Q(sender=sender_id) & models.Q(receiver=receiver_id)) |
            (models.Q(sender=receiver_id) & models.Q(receiver=sender_id))
        ).order_by('timestamp').all()

        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request,sender_id,receiver_id):
        """
        Send a chat message from the logged-in user to a specific receiver.
        """
        user = sender_id
        receiver_id=receiver_id
        data = request.data
        data['sender'] = user 
        data['receiver']= receiver_id# Set the sender to the logged-in user

        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChattedUsersAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request,userid):
        """
        Get a list of users the logged-in user has chatted with.
        """
        user = userid  # Logged-in user
        print(user)
        
        # Fetch all users the logged-in user has sent or received messages with
        sent_chats = Chat.objects.filter(sender=user).values_list('receiver', flat=True)
        received_chats = Chat.objects.filter(receiver=user).values_list('sender', flat=True)
        
        # Combine and get unique user IDs
        chatted_user_ids = set(sent_chats) | set(received_chats)
        
        # Fetch user details for these IDs
        chatted_users = Login_model.objects.filter(id__in=chatted_user_ids)
        
        # Serialize the user details
        serializer = ChattedUsersSerializer1(chatted_users, many=True)
        print(serializer.data)
        
        return Response(serializer.data)


class UserListView(APIView):
    def get(self, request):
        users = user_model.objects.all()  # Get all users
        serializer = UserSerializer1(users, many=True)
        return Response(serializer.data)

        from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.crypto import get_random_string
from .models import Login_model

class ForgotPasswordView(View):
    def get(self, request):
        print("###########")
        return render(request, 'AUTHORITY/forgot_password.html')

    def post(self, request):
        email = request.POST.get('email')
        print ("##########gbfhfhgfhgfhgfhgf#")
        # try:
        user = Login_model.objects.get(Username=email)  # Assuming email is stored in Username
        otp = get_random_string(length=6, allowed_chars='0123456789')
        print("asdfgh")  # Generate a 6-digit OTP
        
        user.Otp = otp
        user.save()
        
        # Send OTP email
        subject = "Password Reset OTP"
        message = f"Your OTP for password reset is: {otp}. It is valid for 5 minutes."
        from_email = "no-reply@yourdomain.com"
        send_mail(subject, message, from_email, [email])
        
        messages.success(request, "OTP has been sent to your email.")
        return redirect('verify-otp')

        # except Login_model.DoesNotExist:
        #     messages.error(request, "No user found with that email.")
        #     return render(request, 'AUTHORITY/forgot_password.html')
class VerifyOTPView(View):
    def get(self, request):
        print("asdfghjkl")
        return render(request, 'AUTHORITY/verify_otp.html')

    def post(self, request):
        print("%%%%%%%%%%%%")
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        print(new_password,confirm_password)

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request,'AUTHORITY/verify_otp.html')

        try:
            user = Login_model.objects.filter(Username=email).first()

            if user.Otp == otp:
                user.Password = new_password  # Store password directly (Hashing should be done for security)
                user.Otp = None  # Clear OTP after reset
                user.save()
                messages.success(request, "Password changed successfully. You can now log in.")
                return redirect('login')

            else:
                messages.error(request, "Invalid OTP.")
                return render(request, 'verify_otp.html')

        except Login_model.DoesNotExist:
            messages.error(request, "Invalid email or OTP.")
            return render(request, 'verify_otp.html')