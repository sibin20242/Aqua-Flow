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

from rest_framework import serializers
from .models import user_model

class UserSerializer1(serializers.ModelSerializer):
    user_login_id=serializers.IntegerField(source='LOGIN.id',read_only=True)
    class Meta:
        model = user_model
        fields = ['id', 'First_name', 'Address','Phone_no', 'Mail', 'user_login_id']



class signupSerializer (ModelSerializer): 
    class Meta:  
        model =user_model
        fields = ['Mail']

class StatusSerializer (ModelSerializer): 
    class Meta:  
        model =application_model
        fields = ['Status']



class TimeSerializer (ModelSerializer): 
    class Meta:  
        model = time_model  
        fields = ['Date','morning_Time','evening_Time','description']


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
    First_name = serializers.SerializerMethodField()  # Add a custom field for the name

    class Meta:
        model = Login_model
        fields = ['id', 'username', 'type', 'First_name']  # Include the custom name field

    def get_First_name(self, obj):
        # Fetch the related UserTable instance for the given LoginTable instance
        user = user_model.objects.filter(LOGIN=obj).first()
        return user.First_name if user else None        



class ChatSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')
    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp', 'sender_username', 'receiver_username']
class ChattedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_model
        fields = ['id', 'Username']
class ChattedUsersSerializer1(serializers.ModelSerializer):
    First_name = serializers.SerializerMethodField()  # Add a custom field for the name

    class Meta:
        model = Login_model
        fields = ['id', 'Username','First_name']  # Include the custom name field

    def get_First_name(self, obj):
        # Fetch the related UserTable instance for the given LoginTable instance
        user = user_model.objects.filter(LOGIN=obj).first()
        return user.First_name if user else None