from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from AquaFlowApp.models import *
from rest_framework import serializers

class UserSerializer (ModelSerializer):
    class Meta:  
        model = user_model  
        fields = ['First_name', 'Mid_name','Last_name','Area','Mail','Pincode','Address','Panchayath_name','Profile','Phone_no']

class LoginSerializer (ModelSerializer): 
    class Meta:  
        model = Login_model  
        fields = ['Username','Password']





class signupSerializer (ModelSerializer): 
    class Meta:  
        model =user_model
        fields = ['Mail']


# class HomeuserSerializer (ModelSerializer): 
#     class Meta:  
#         model = ViewStatus  
#         fields = ['']



class TimeSerializer (ModelSerializer): 
    class Meta:  
        model = time_model  
        fields = ['Date','Time','description','Area']


class BillSerializer (ModelSerializer): 
    class Meta:  
        model = bill_model  
        fields = ['USER','Previous_MeterReading','Current_MeterReading','Total_Usage','Fixed_Charge','Prior_Obligation','Advance','Fine','Total_Amount']


class ProfileSerializer (ModelSerializer):
     class Meta:  
        model = user_model  
        fields = ['First_name', 'Mid_name','Last_name','Mail','Pincode','Address','Profile','Phone_no']


class ViewProfileSerializer (ModelSerializer):
     class Meta:  
        model = user_model  
        fields = ['Name','Consumer_no']



class ComplaintSerializer (ModelSerializer): 
    class Meta:  
        model = complaints_model  
        fields = ['USER','Complaints','complaint_type']


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
        fields = ['Application_no','Panchayath_name','Father_name',  'Address', 'Phone_no' , 'Family_members',  'Adhar_no' , 'Rationcard', 'Neighbourconsumer_no',  'Cast', 'Aadhaar_photo' , 'Rationcard_photo' , 'Ownershipcertificate_photo' ]  


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
        fields = ['USER','Rating','Feedback']

class ChatSerializer(ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp', 'sender_username', 'receiver_username']


class ChatSerializer1(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['sender', 'receiver', 'message']
class ChattedUsersSerializer(ModelSerializer):
    class Meta:
        model = Login_model
        fields = ['id', 'username', 'type']
class ChattedUsersSerializer1(ModelSerializer):
    name = serializers.SerializerMethodField()  # Add a custom field for the name

    class Meta:
        model = Login_model
        fields = ['id', 'username', 'type', 'name']  # Include the custom name field

    def get_name(self, obj):
        # Fetch the related UserTable instance for the given LoginTable instance
        user = UserTable.objects.filter(LOGINID=obj).first()
        return user.name if user else None        