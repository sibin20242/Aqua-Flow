class Addauthority_form(ModelForm):
    class Meta:
        model = authority_model
        fields = ('First_name', 'Mid_name', 'Last_name', 'address')