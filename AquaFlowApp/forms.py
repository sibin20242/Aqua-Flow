from django.forms import ModelForm 
from .models import * 


class LoginForm(ModelForm):
    class Meta:
        model = Login_model
        fields = ('Username', 'Password')


class ProfileForm(ModelForm):
    class Meta:
        model = authority_model
        fields = ('First_name', 'Mid_name','Last_name','Area','Mail','Pincode','Address','Panchayath_name','Profile','Phone_no')

