from django import forms
from home.models import Profiledetail

class ProfiledetailForm(forms.ModelForm):
    class Meta:
        model = Profiledetail
        fields = ('email', 'firstname', 'middlename', 'lastname', 'dob', 'gender', 'phone', 'address', 'address2', 'country', 'statename', 'city', 'zipf',  )