from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from AquaFlowApp.models import *

class UserSerializer (ModelSerializer):
    class Meta:  
        model = user_model  
        fields = ['First_name', 'Mid_name','Last_name','Area','Mail','Pincode','Address','Panchayath_name','Profile','Phone_no']

class LoginSerializer (ModelSerializer): 
    class Meta:  
        model = Login_model  
        fields = ['Username','Password']





class signupupSerializer (ModelSerializer): 
    class Meta:  
        model =user_model 
        fields = ['username','email','password','re-password']


# class HomeuserSerializer (ModelSerializer): 
#     class Meta:  
#         model = ViewStatus  
#         fields = ['']



class TimeSerializer (ModelSerializer): 
    class Meta:  
        model = time_model  
        fields = ['Date','Time']


class BillSerializer (ModelSerializer): 
    class Meta:  
        model = bill_model  
        fields = ['USER','Previous_MeterReading','Current_MeterReading','Total_Usage','Fixed_Charge','Prior_Obligation','Advance','Fine','Total_Amount']


class ProfileSerializer (ModelSerializer):
     class Meta:  
        model = user_model  
        fields = ['First_name', 'Mid_name','Last_name','Area','Mail','Pincode','Address','Panchayath_name','Profile','Phone_no']



class ComplaintSerializer (ModelSerializer): 
    class Meta:  
        model = complaints_model  
        fields = ['USER','Complaints']


class AssignedworkSerializer (ModelSerializer): 
    class Meta:  
        model = assignedwork_model  
        fields = ['USER','area','work']


class UserdetailsSerializer (ModelSerializer): 
    class Meta:  
        model = user_model  
        fields = ['User_Name','Consumer_NO','Phone_No']


class ApplicationSerializer (ModelSerializer): 
    class Meta:  
        model = application_model  
        fields = ['USER', 'Application_no','Status','Panchayath_name',' Father_name', 'Mother_name', 'Address', 'Phone_no' , 'Family_members',  'Adhar_no' , 'Rationcard', 'Neighbourconsumer_no',  'Cast', 'Aadhaar_photo' , 'Rationcard_photo' , 'Ownershipcertificate_photo' ]  


class UpdateReportSerializer (ModelSerializer): 
    class Meta:  
        model = report_model  
        fields = ['STAFF','Consumer_no','Complaint_no','Upload_photo']

class MeterReadingSerializer (ModelSerializer):
    class Meta:  
        model = reading_model  
        fields = ['USER','STAFF','revious_MeterReading','Current_MeterReading','Total_Usage','Fixed_Charge','Prior_Obligation','Advance','Fine','Total_Amount']

class FeedbackSerializer (ModelSerializer): 
    class Meta:  
        model = feedback_model  
        fields = ['USER','Consumer_no','Complaint_no']