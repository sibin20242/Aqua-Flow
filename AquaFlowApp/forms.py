from django.views import ModelForm 

class LoginForm(ModelForm):
    class Meta:
        model = Login_model
        fields = ('Username', 'Password')