from django.db import models

# Create your models here.

class Login_model(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)

class area_model(models.Model):
    Area = models.CharField(max_length=100, null=True, blank=True)

class authority_model(models.Model):
    LOGIN = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    AREA = models.ForeignKey(area_model, on_delete=models.CASCADE, null=True, blank=True)
    First_name = models.CharField(max_length=100, null=True, blank=True)
    Mid_name = models.CharField(max_length=100, null=True, blank=True)
    Last_name = models.CharField(max_length=100, null=True, blank=True)
    Area = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Panchayath_name = models.CharField(max_length=100, null=True, blank=True)
    Profile = models.FileField(upload_to='profile/', null=True, blank=True)
    Phone_no = models.IntegerField(null=True, blank=True)

class staff_model(models.Model):
    LOGIN = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    AUTHORITY = models.ForeignKey(authority_model, on_delete=models.CASCADE, null=True, blank=True)
    AREA = models.ForeignKey(area_model, on_delete=models.CASCADE, null=True, blank=True)
    First_name = models.CharField(max_length=100, null=True, blank=True)
    Mid_name = models.CharField(max_length=100, null=True, blank=True)
    Last_name = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Profile = models.FileField(upload_to='profile/',null=True, blank=True)
    Phone_no = models.IntegerField(null=True, blank=True)



   


class user_model(models.Model):
    LOGIN = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    First_name = models.CharField(max_length=100, null=True, blank=True)
    Mid_name = models.CharField(max_length=100, null=True, blank=True)
    Last_name = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Consumer_no = models.CharField(max_length=100, null=True, blank=True)
    Profile = models.FileField(upload_to='profile/',null=True, blank=True)
    Phone_no = models.IntegerField(null=True, blank=True)

class time_model(models.Model):
    Area = models.CharField(max_length=100, null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)
    Date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=100, null=True, blank=True)


class assignedwork_model(models.Model):
    STAFF = models.ForeignKey(staff_model, on_delete=models.CASCADE, null=True, blank=True)
    Area = models.CharField(max_length=100, null=True, blank=True)
    Work = models.CharField(max_length=100, null=True, blank=True)


class report_model(models.Model):
    STAFF = models.ForeignKey(staff_model, on_delete=models.CASCADE, null=True, blank=True)
    Consumer_no = models.CharField(max_length=100, null=True, blank=True)
    Complaint_no = models.CharField(max_length=100, null=True, blank=True)
    Upload_photo = models.FileField(upload_to='photo/',null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

class reading_model(models.Model):
    STAFF = models.ForeignKey(staff_model, on_delete=models.CASCADE, null=True, blank=True)
    USER = models.ForeignKey(user_model, on_delete=models.CASCADE, null=True, blank=True)
    Current_reading = models.IntegerField(null=True, blank=True)
    Total_usage = models.IntegerField(null=True, blank=True)
    Fixed_charge = models.IntegerField(null=True, blank=True)
    Advance = models.IntegerField(null=True, blank=True)    
    Prior_obligation = models.IntegerField(null=True, blank=True)
    Fine = models.IntegerField(null=True, blank=True)
    Total_amount = models.IntegerField(null=True, blank=True)

class application_model(models.Model):
    USER = models.ForeignKey(user_model, on_delete=models.CASCADE, null=True, blank=True)
    Application_no = models.IntegerField(null=True, blank=True)
    Status = models.CharField(max_length=100, null=True, blank=True)
    Panchayath_name = models.CharField(max_length=100, null=True, blank=True)
    Father_name = models.CharField(max_length=100, null=True, blank=True)
    Mother_name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone_no = models.IntegerField(null=True, blank=True)
    Family_members = models.IntegerField(null=True, blank=True)
    Adhar_no = models.IntegerField(null=True, blank=True)
    Rationcard = models.CharField(max_length=100, null=True, blank=True)
    Neighbourconsumer_no = models.IntegerField(null=True, blank=True)
    Cast = models.CharField(max_length=100, null=True, blank=True)
    Adhar_photo = models.FileField(upload_to='photo/',null=True, blank=True)
    Rationcard_photo = models.FileField(upload_to='photo/',null=True, blank=True)
    Ownershipcertificate_photo = models.FileField(upload_to='photo/', null=True, blank=True)
   

class complaints_model(models.Model):
    USER = models.ForeignKey(user_model, on_delete=models.CASCADE, null=True, blank=True)  
    Complaints= models.CharField(max_length=100, null=True, blank=True)
    Reply = models.FileField(max_length=100, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)

class feedback_model(models.Model):
    USER = models.ForeignKey(user_model, on_delete=models.CASCADE, null=True, blank=True)
    Feedback = models.CharField(max_length=100, null=True, blank=True)
    Rating = models.FloatField(null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)

class chat_model(models.Model):
    FROMID = models.ForeignKey(Login_model, on_delete=models.CASCADE,related_name='fromid', null=True, blank=True)
    TOID = models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)

   
class bill_model(models.Model):
    USER = models.ForeignKey(user_model, on_delete=models.CASCADE, null=True, blank=True)
    READING = models.ForeignKey(reading_model, on_delete=models.CASCADE, null=True, blank=True)
    Payment_status = models.CharField(max_length=100, null=True, blank=True)
    Date = models.DateField(auto_now_add=True)
    Due_date = models.DateTimeField(auto_now_add=True)
    









    







    


    





