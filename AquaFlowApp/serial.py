

class UserSerializer (ModelSerializer):
    class Meta:
        model = user_model
        fields = ['First_name', 'Mid_name','Last_name','Area','Mail','Pincode','Address','Panchayath_name','Profile','Phone_no']


class StatusSerializer (ModelSerializer):
    class Meta:
        model = ViewStatus
        fields = ['']


class TimeSerializer (ModelSerializer):
    class Meta:
        model = time_model
        fields = ['Date','Time']


class BillSerializer (ModelSerializer):
    class Meta:
        model = bill_model
        fields = ['Previous_MeterReading','Current_MeterReading','Total_Usage','Fixed_Charge','Prior_Obligation','Advance','Fine','Total_Amount']


class ProfileSerializer (ModelSerializer):
    class Meta:
        model = user_model
        fields = ['First_name', 'Mid_name','Last_name','Area','Mail','Pincode','Address','Panchayath_name','Profile','Phone_no']



class ComplaintSerializer (ModelSerializer):
    class Meta:
        model = complaints_model
        fields = ['Complaints']


class AssignedworkSerializer (ModelSerializer):
    class Meta:
        model = assignedwork_model
        fields = ['area','work']


class UserdetailsSerializer (ModelSerializer):
    class Meta:
        model = user_model
        fields = ['User_Name','Consumer_NO','Phone_No']

